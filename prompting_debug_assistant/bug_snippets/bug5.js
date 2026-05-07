for (var i = 0; i < 3; i++) {
    setTimeout(() => {
        // Xəta: 'var' istifadə olunduğu üçün hamısında 3 çap olunacaq
        console.log("Counter:", i);
    }, 1000);
}
