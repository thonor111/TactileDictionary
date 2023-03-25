// In this file you can specify the trial data for your experiment


const key_press_trials = [
    {
        question: "Press the according button",
        picture: "images/red.png",
        type: 'vision',
        key1: '9',
        key2: '7',
        9: 'red or high pitch',
        7: 'green or low pitch',
        expected: 'red or high pitch'
    },
    {
        question: "Press the according button",
        picture: 'images/green.png',
        type: 'vision',
        key1: '9',
        key2: '7',
        9: 'red or high pitch',
        7: 'green or low pitch',
        expected: 'green or low pitch'
    },
    {
        question: "Press the according button",
        picture: 'images/sound.jpg',
        pitch: 0,
        type: 'sound',
        key1: '9',
        key2: '7',
        9: 'red or high pitch',
        7: 'green or low pitch',
        expected: 'red or high pitch'
    },
    {
        question: "Press the according button",
        picture: 'images/sound.jpg',
        pitch: 1,
        type: 'sound',
        key1: '9',
        key2: '7',
        9: 'red or high pitch',
        7: 'green or low pitch',
        expected: 'green or low pitch'
    }
];

const key_press_trials_audio = [
    {
        question: "Press the according button",
        pitch: 0,
        sound: 1,
        key1: '9',
        key2: '7',
        9: 'red or high pitch',
        7: 'green or low pitch',
        expected: 'red or high pitch'
    },
    {
        question: "Press the according button",
        pitch: 1,
        sound: 1,
        key1: '9',
        key2: '7',
        9: 'red or high pitch',
        7: 'green or low pitch',
        expected: 'green or low pitch'
    }
];
