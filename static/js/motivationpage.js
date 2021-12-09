let randomNum = 0;
const images = ['/static/images/arnold.jfif', '/static/images/cbum.jfif', '/static/images/ronnie.jpg',
        '/static/images/rocky.jfif']

const audio = ['/static/audio/arnold.mp3', '/static/audio/cbum.mp3', '/static/audio/Ronnie.mp3',
        '/static/audio/rocky.mp3']



$(document).ready(function () {
    function random() {
        switch (randomNum) {
            case 1:
                $('img').attr('src', '/static/images/motivation.jfif');
                $('audio').attr('src' ,'/static/audio/quitting.mp3');
                break;
            case 2:
                $('img').attr('src', '/static/images/cbum.jfif');
                $('audio').attr('src' ,'/static/audio/cbum.mp3');
                break;
            case 3:
                $('img').attr('src', '/static/images/ronnie.jpg');
                $('audio').attr('src' , '/static/audio/Ronnie.mp3');
                break;
            case 4:
                $('img').attr('src', '/static/images/rocky.jfif');
                $('audio').attr('src' ,'/static/audio/rocky.mp3');
                break;
            case 5:
                $('img').attr('src', '/static/images/arnold.jfif');
                $('audio').attr('src' ,'/static/audio/arnold.mp3');
                break;
            default:
                $('img').attr('src', '/static/images/run.jfif');
                $('audio').attr('src' ,'');
                break;
        }
    }

    $('#motivation-button').click(function () {
        console.log(randomNum);
        randomNum = Math.floor(Math.random() * 4) + 1;
        random();
    });
});
