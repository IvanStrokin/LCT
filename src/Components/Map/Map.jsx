import React, { useEffect } from 'react'

import { load } from '@2gis/mapgl';

export const Map = () => {
    useEffect(() => {
        let map;
        load().then((mapglAPI) => {
            map = new mapglAPI.Map('map-container', {
                center: [55.31878, 25.23584],
                zoom: 13,
                key: '3508d4c8-2457-4053-a51a-a5a2d0d5d00c',
            });
        });

        // Удаляем карту при размонтировании компонента
        return () => map && map.destroy();
    }, []);

    const MapWrapper = React.memo(
        () => {
            return <div id="map-container" style={{ width: '100%', height: '100%' }}></div>;
        },
        () => true,
    );

    return (
        <div style={{ width: '100%', height: '600px' }}>
            <MapWrapper/>
        </div>
    );
};