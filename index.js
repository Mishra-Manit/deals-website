fetch("test1.json")
    .then(response => response.json())
    .then(data => {
        console.log(data[0][0])

        //i = 1

        for (var i = 0; i <= 7; i++){
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

        i = 8
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

            for (var i = 9; i <= 12; i++){
                document.querySelector("#name-" + i.toString()).innerText = data[i-9][0];
                document.querySelector("#image-" + i.toString()).src = data[i-9][5];
                document.querySelector("#price-" + i.toString()).innerText = data[i-9][3];
                document.querySelector("#newPrice-" + i.toString() ).innerText = data[i-9][2];
                document.querySelector("#sale-" + i.toString()).href = data[i-9][1];
                document.querySelector("#percentOff-" + i.toString()).innerText = data[i-9][4];
            }
            
        })






