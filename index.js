fetch("test1.json")
    .then(response => response.json())
    .then(data => {
        console.log(data[0][0])

        //i = 1

        for (var i = 0; i <= 12; i++){
            document.querySelector("#name-" + i.toString()).innerText = data[i][0];
            document.querySelector("#image-" + i.toString()).src = data[i][5];
            document.querySelector("#price-" + i.toString()).innerText = data[i][3];
            document.querySelector("#newPrice-" + i.toString() ).innerText = data[i][2];
            document.querySelector("#sale-" + i.toString()).href = data[i][1];
            document.querySelector("#percentOff-" + i.toString()).innerText = data[i][4];
        }
        
    })

fetch("bestbuyDealOfDay.json")
    .then(response => response.json())
    .then(data => {

        i = 13
        document.querySelector("#name-" + i.toString()).innerText = data[0];
        document.querySelector("#image-" + i.toString()).src = data[5];
        document.querySelector("#price-" + i.toString()).innerText = data[3];
        document.querySelector("#newPrice-" + i.toString() ).innerText = data[2];
        document.querySelector("#sale-" + i.toString()).href = data[1];
        document.querySelector("#percentOff-" + i.toString()).innerText = data[4];        
    })

fetch("bestbuy.json")
    .then(response => response.json())
    .then(data => {

        //i = 1

        for (var i = 14; i <= 16; i++){
            document.querySelector("#name-" + i.toString()).innerText = data[i-14][0];
            document.querySelector("#image-" + i.toString()).src = data[i-14][5];
            document.querySelector("#price-" + i.toString()).innerText = data[i-14][3];
            document.querySelector("#newPrice-" + i.toString() ).innerText = data[i-14][2];
            document.querySelector("#sale-" + i.toString()).href = data[i-14][1];
            document.querySelector("#percentOff-" + i.toString()).innerText = data[i-14][4];
        }
        
    })

fetch("walmart.json")
    .then(response => response.json())
    .then(data => {

        for (var i = 18; i <= 25; i++){
            document.querySelector("#name-" + i.toString()).innerText = data[i-18][0];
            document.querySelector("#image-" + i.toString()).src = data[i-18][4];
            document.querySelector("#price-" + i.toString()).innerText = data[i-18][3];
            document.querySelector("#newPrice-" + i.toString() ).innerText = data[i-18][2];
            document.querySelector("#sale-" + i.toString()).href = data[i-18][1];
        }
    })






