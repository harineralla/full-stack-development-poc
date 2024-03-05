import React, { useState, useEffect } from 'react';
import '../App.css';

function Time() {
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('/time').then(res => res.json()).then(data => {
            setCurrentTime(data.time);
        });
    }, []);

    return (
        <div className="App">
            <p>The current time is {currentTime}.</p>
        </div>
    );
}

export default Time;