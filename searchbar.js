function validate(form) {
  if(form.username.value == "admin1" && form.password.value == "admin")
  {
    window.open('admin.html')
  }
  else if (form.username.value == "user1" && form.password.value == "user")
  {
    window.open('home.html')
  }
  else{
    window.alert('Username or password incorrect')
  }
}


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

//table sort function..//
function sortTable(n) {
  var table, rows, d, x, y, rearrange, arrange;
  table = document.getElementById("staffRecord");
  rearrange = true;
  while (rearrange) {
    rearrange = false;
    rows = table.rows;
    
    for (d = 1; d < (rows.length - 1); d++) {
      arrange = false;
      x = rows[d].getElementsByTagName("td")[n];
      y = rows[d + 1].getElementsByTagName("td")[n];
      if (Number(x.innerHTML) > Number(y.innerHTML)) {
        arrange = true;
        break;
      }
    }
    if (arrange) {
      rows[d].parentNode.insertBefore(rows[d + 1], rows[d]);
      rearrange = true;
    }
  }
}