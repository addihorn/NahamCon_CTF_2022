for (let i = 1000000000000000; i< 9332654729891548; i++) { //5306108
    console.log("Number to check:" + i)
    if ( parseFloat(i).toPrecision(16) == parseFloat(i -1).toPrecision(16) ) {
        console.log(i);
        break;
    }
}
