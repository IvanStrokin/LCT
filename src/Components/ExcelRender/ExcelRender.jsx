import React, { Component } from "react";
import { Table, Button, Popconfirm, Row, Col, Icon, Upload } from "antd";
import { ExcelRenderer } from "react-excel-renderer";
import { EditableFormRow, EditableCell } from "./editable";

export default class ExcelPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedRowKeys: [],
            loading : false,
            cols: [],
            rows: [],
            newSelectedRowKeys : null,
            errorMessage: null,
            columns: [
                {
                    title: "Местоположение",
                    dataIndex: "location",
                    editable: true
                },
                {
                    title: "Количество комнат",
                    dataIndex: "numberOfRooms",
                    editable: true
                },
                {
                    title: "Сегмент",
                    dataIndex: "segment",
                    editable: true
                },
                {
                    title: "Этажность дома",
                    dataIndex: "floors",
                    editable: true
                },
                {
                    title: "Материал стен",
                    dataIndex: "wallMaterial",
                    editable: true
                },
                {
                    title: "Этаж расположения",
                    dataIndex: "floorLocation",
                    editable: true
                },
                {
                    title: "Площадь квартиры, кв.м",
                    dataIndex: "square",
                    editable: true
                },
                {
                    title: "Площадь кухни, кв.м",
                    dataIndex: "square1",
                    editable: true
                },
                {
                    title: "Наличие балкона/лоджии",
                    dataIndex: "balcony",
                    editable: true
                },
                {
                    title: "Удаленность от станции метро",
                    dataIndex: "distance",
                    editable: true
                },
                {
                    title: "Состояние",
                    dataIndex: "condition",
                    editable: true
                },
                {
                    title: "Действия",
                    dataIndex: "action",
                    render: (text, record) =>
                        this.state.rows.length >= 1 ? (
                            <div>
                                <div>
                                    <Popconfirm
                                        title="Точно удалить?"
                                        onConfirm={() => this.handleDelete(record.key)}
                                    >
                                        <Icon
                                            type="delete"
                                            theme="filled"
                                            style={{ color: "red", fontSize: "20px" }}
                                        />
                                    </Popconfirm>
                                </div>
                            </div>




                        ) : null,

                }
            ]
        };
    }

    handleSave = row => {
        const newData = [...this.state.rows];
        const index = newData.findIndex(item => row.key === item.key);
        const item = newData[index];
        newData.splice(index, 1, {
            ...item,
            ...row
        });
        this.setState({ rows: newData });
    };

    fileHandler = fileList => {
        console.log("fileList", fileList);
        let fileObj = fileList;
        if (!fileObj) {
            this.setState({
                errorMessage: "No file uploaded!"
            });
            return false;
        }
        console.log("fileObj.type:", fileObj.type);
        if (
            !(
                fileObj.type === "application/vnd.ms-excel" ||
                fileObj.type ===
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        ) {
            this.setState({
                errorMessage: "Unknown file format. Only Excel files are uploaded!"
            });
            return false;
        }

        ExcelRenderer(fileObj, (err, resp) => {
            if (err) {
                console.log(err);
            } else {
                let newRows = [];
                resp.rows.slice(1).map((row, index) => {
                    if (row && row !== "undefined") {
                        newRows.push({
                            key: index,
                            location : row[0],
                            numberOfRooms: row[1],
                            segment: row[2],
                            floors: row[3],
                            wallMaterial: row[4],
                            floorLocation : row[5],
                            square: row[6],
                            square1: row[7],
                            balcony: row[8],
                            distance: row[9],
                            condition: row[10],
                        });
                    }
                });
                if (newRows.length === 0) {
                    this.setState({
                        errorMessage: "No data found in file!"
                    });
                    return false;
                } else {
                    this.setState({
                        cols: resp.cols,
                        rows: newRows,
                        errorMessage: null
                    });
                }
            }
        });
        return false;
    };

    handleSubmit = async () => {
        console.log("submitting: ", this.state.rows);
        //submit to API
        //Если успешно, поменять исходный пулл на пулл от бэков
        //this.setState({ })
    };

    handleSubmit1 = async () => {
        console.log("submitting: ", this.state.selectedKeys);
        //Отправить пулл выбранных обьектов на сервер
        //
    };

    handleDelete = key => {
        const rows = [...this.state.rows];
        this.setState({ rows: rows.filter(item => item.key !== key) });
    };

    handleSelect = key => {
        this.setState({ rows: [] })
    };

    handleAdd = () => {
        const { count, rows } = this.state;
        const newData = {
            key: count,
        };
        this.setState({
            rows: [newData, ...rows],
            count: count + 1
        });
    };

    render() {
        const components = {
            body: {
                row: EditableFormRow,
                cell: EditableCell
            }
        };
        const columns = this.state.columns.map(col => {
            if (!col.editable) {
                return col;
            }
            return {
                ...col,
                onCell: record => ({
                    record,
                    editable: col.editable,
                    dataIndex: col.dataIndex,
                    title: col.title,
                    handleSave: this.handleSave,
                })
            };
        });



        return (
            <>
                <h1>Тестовый образец</h1>
                <Row gutter={16}>
                    <Col
                        span={8}
                        style={{
                            display: "flex",
                            justifyContent: "space-between",
                            alignItems: "center",
                            marginBottom: "5%"
                        }}
                    >
                        <div style={{ display: "flex", alignItems: "center" }}>
                            <div className="page-title">Сервис для
                                расчета рыночной стоимости
                                жилой недвижимости
                                города Москва</div>
                        </div>
                    </Col>
                    <Col
                        span={8}
                        align="right"
                        style={{ display: "flex", justifyContent: "space-between" }}
                    >
                        {this.state.rows.length > 0 && (
                            <>
                                <Button
                                    onClick={this.handleAdd}
                                    size="large"
                                    type="info"
                                    style={{ marginBottom: 16 }}
                                >
                                    <Icon type="plus" />
                                    Добавить объект
                                </Button>{" "}
                                <Button
                                    onClick={this.handleSubmit}
                                    size="large"
                                    type="primary"
                                    style={{ marginBottom: 16, marginLeft: 10 }}
                                >
                                    Рассчитать пулл обьектов
                                </Button>
                            </>
                        )}
                    </Col>
                </Row>
                <Button type="primary" onClick={this.handleSubmit1} disabled={this.state.selectedRowKeys.length > 0} loading={this.loading}>
                    Рассчитать по эталонным обьектам
                </Button>
                <div>
                    <Upload
                        name="file"
                        beforeUpload={this.fileHandler}
                        onRemove={() => this.setState({ rows: [] })}
                        multiple={false}
                        accept='.xlsx'
                    >
                        <Button>
                            <Icon type="upload"/> Нажмите, чтобы загрузить исходный пулл обьектов
                            <Icon
                                type='file-excel'
                                size="large"
                            />
                        </Button>
                    </Upload>
                </div>
                <div style={{ marginTop: 20 }}>
                    <Table
                        components={components}
                        rowClassName={() => "editable-row"}
                        dataSource={this.state.rows}
                        columns={columns}
                        rowSelection={{}}
                    />
                </div>
            </>
        );
    }
}
