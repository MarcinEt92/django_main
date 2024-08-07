class Timer {

    static getTime() {
        let date = new Date();
        let day = date.getDay();
        let month = date.getMonth();
        let year = date.getFullYear();

        let hour = date.getHours();
        if (hour < 10) hour = "0" + hour;

        let minute = date.getMinutes();
        if (minute < 10) minute = "0" + minute;

        let seconds = date.getSeconds();
        if (seconds < 10) seconds = "0" + seconds;

        return `${day}/${month}/${year}, ${hour}:${minute}:${seconds}`
    }
    
    static update() {
        const timerDiv = document.querySelector("#time");
        timerDiv.innerHTML = Timer.getTime();
    }

    static runner() {
        Timer.update();
        setTimeout(Timer.runner, 1000);
    }
}

class Main {
    static run() {
        Timer.runner();
    }
}

Main.run();
