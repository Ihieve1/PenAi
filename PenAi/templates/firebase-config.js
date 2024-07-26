// firebase-config.js

// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-analytics.js";

const firebaseConfig = {
    apiKey: "AIzaSyBnqiphyNW22iJHDE78mGccvnUnubZ5xEA",
    authDomain: "penai-45582.firebaseapp.com",
    projectId: "penai-45582",
    storageBucket: "penai-45582.appspot.com",
    messagingSenderId: "814415327072",
    appId: "1:814415327072:web:64935656d24c2a4a527805",
    measurementId: "G-BJFD578BR2"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
