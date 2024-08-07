
class SliderPosition {

    static sliderData = {
        numberOfImages: 5,
        slideWidthInPx: 600,
        borderWidthInPx: 5,
        positionInPx: 0
    }

    static previous() {
        const slider = document.querySelector("#slides-pos");
        let newPosition = this.sliderData["positionInPx"] + this.sliderData["slideWidthInPx"];

        if (newPosition > 0) {
            newPosition = 0;
        }

        this.sliderData["positionInPx"] = newPosition;
        slider.style.left = `${newPosition}px`;
    }

    static next() {
        const slider = document.querySelector("#slides-pos");
        let newPosition = this.sliderData["positionInPx"] - this.sliderData["slideWidthInPx"];
        const sliderMaxPosition = this.sliderData["slideWidthInPx"] * (this.sliderData["numberOfImages"] - 1);

        if (-newPosition > sliderMaxPosition) {
            newPosition = -sliderMaxPosition;
        }

        this.sliderData["positionInPx"] = newPosition;
        slider.style.left = `${newPosition}px`;
    }

    static run() {
        document.querySelector("#prev-pos").addEventListener("click", (event) => {
            event.preventDefault();
            this.previous();
        });

        document.querySelector("#next-pos").addEventListener("click", (event) => {
            event.preventDefault();
            this.next();
        });
    }
}

class SliderOpacity {

    static sliderData = {
        numberOfImages: 5,
        currentSlide: 1
    }

    static setOpacity(currentSlide) {

        // set all opacities to 0 then set current opacity to 1
        for (let i = 1; i <= this.sliderData["numberOfImages"]; i++) {
            let slide = document.querySelector(`#img${i}`);
            slide.style.opacity = 0;
        }
        document.querySelector(`#img${currentSlide}`).style.opacity = 1;
    }

    static next() {
        let currentSlide = this.sliderData["currentSlide"] + 1;

        if (currentSlide > 5) {
            currentSlide = 1;
        }

        this.sliderData["currentSlide"] = currentSlide;
        this.setOpacity(currentSlide);
    }

    static run() {
        setInterval(() => {
            this.next();
        }, 3000);
    }
}

class Main {
    static run() {
        SliderPosition.run();
        SliderOpacity.run();
    }
}

Main.run();
