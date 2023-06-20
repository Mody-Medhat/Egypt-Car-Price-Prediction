
function change_color(labl, checkboxName, labelname) {

    clr = document.getElementsByName(checkboxName);
    labls2 = document.getElementsByName(labelname);


    for (var i = 0; i < clr.length; i++) {

        if (clr[i].type === 'radio' && clr[i].checked) {
            labl.style.backgroundColor = "#2091f1";
            clr[i].style.color = "#F77D0A"
        } else {
            for (var e = 0; e < labls2.length; e++) {
                if (labls2[e] != labl) {
                    labls2[e].style.backgroundColor = "";
                }
            }
            clr[i].style.color = ""
        }

    }
}


$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})

// $(document).ready(function () {
//     // Initialize select2
//     $("#brand").select2();
//     $("#model").select2();
//     $("#color").select2();


// });

$(document).ready(function () {
    $("#year").datepicker({
        format: "yyyy",
        viewMode: "years",
        minViewMode: "years",
        autoclose: true
    });
})

$(document).ready(function () {
    $('.select2').select2({
        templateResult: formatOption
    });
});
function formatOption(option) {
    if (!option.id) {
        return option.text;
    }
    var filePath = "./static/BrandImg/"; // Add the desired file path here
    var imageSrc = filePath + $(option.element).data('image');
    if (imageSrc) {
        return $('<span><img src="' + imageSrc + '" class="select-image" style="width: 20px; height: 20px;" /> ' + option.text + '</span>');
    } else {
        return option.text;
    }
}

const ColorCode = {
    Blue: "#007bff",
    Gray: "#6c757d",
    White: "#ffffff",
    Mocha: "#6f372d",
    Black: "#000000",
    Gold: "#f9d77e",
    Green: "#00FF00",
    Silver: "#bebdb6",
    'Dark red': "#8B0000",
    Brown: "#35281e",
    Bronze: "#51412d",
    Beige: "#F5F5DC",
    Champagne: "#eed9b6",
    'Dark green': "#006400",
    'Light grey': "#90ee90",
    Beige: "#d9b99b",
   'Dark blue': "#00008b",
    Green: "#245336",
    Eggplant: "#483248",
    Cyan: "#00FFFF",
    Yellow: "#ffc107",
    Petroleum: "#005f6a",
    Purple: "#800080",
    Olive: "#808000",
    Orange: "#FFA500",
};


function PrintData() {
    var brand = document.getElementById("brand").value;

    var model = document.getElementById("model").value;
    console.log(model);
    var year = document.getElementById("year").value;
    var kilometers_Driven = document.getElementById("kilometers_Driven").value;
    var color = document.getElementById("color").value;

    var vehicle_style = document.getElementById("vehicle_style").value;

    BrandModel = brand + " " + model;
    // document.getElementById('brandData').innerHTML = BrandModel;
    console.log(brand + " " + model)
    document.getElementById('brandData').innerHTML = model;
    document.getElementById('yearData').innerHTML = year;
    document.getElementById('kilometers_DrivenData').innerHTML = kilometers_Driven;

    document.getElementById('vehicle_styleData').innerHTML = vehicle_style;
    for (const [key, value] of Object.entries(ColorCode)) {
        if (key == color) {
            document.getElementById("colorData").style.color = value;
        }
    }
    // document.getElementById('colorData').innerHTML = color;
}

function required() {

    // data send from form to card
    const year = document.getElementById('year');
    const engine_cc = document.getElementById('engine_cc');
    const kilometers_Driven = document.getElementById('kilometers_Driven');
    const fule = document.getElementById('fule');
    //  const city_mpg = document.getElementById('city_mpg');


    if (year.value === "") {
        document.getElementById("year_label").style.color = "rgb(255 0 57)";
        document.getElementById("year_label").style.fontWeight = "700";
        year.style.border = "3px solid #ffc107"; 
        y = 0;
    }
    else {
        y = 1;
        year.style.color = null;
    }
    if (engine_cc.value === "") {
        document.getElementById("engine_cc_label").style.color = "rgb(255 0 57)";
        engine_cc.style.border = "3px solid #ffc107"; 
        hp = 0;
    }
    else {
        hp = 1;
    }
    if (kilometers_Driven.value === "") {
        document.getElementById("kilometers_Driven_label").style.color = "rgb(255 0 57)";
        kilometers_Driven.style.border = "3px solid #ffc107"; 
        cy = 0;
    }
    else {
        cy = 1;
    }
    if (fule.value === "") {
        document.getElementById("fule_label").style.color = "rgb(255 0 57)";
        fule.style.border = "3px solid #ffc107"; 
        h = 0;
    }
    else {
        h = 1;
    }
    //return condition//
    if (y == 1 && hp == 1 && cy == 1 && h == 1) {
        return true;
    }
    else
        return false;
}
function valdiateyear(){
    
}
