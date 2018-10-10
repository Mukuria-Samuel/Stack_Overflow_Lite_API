// NB:when the function is called, getting the list id has to come first before the list item //
function myFunction() {
    var product, convert, li, ul, a, item;
    product = document.getElementById("products");//searchbar//
    convert = product.value.toUpperCase();
    ul = document.getElementById("products_list");//list id//
    li = ul.getElementsByTagName("li");
   

    // list iteration..//
    for (item = 0; item < li.length; item++) {
        a = li[item].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(convert) > -1) {
            li[item].style.display = "";
        } else {
            li[item].style.display = "none";
        }
    }
}