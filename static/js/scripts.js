
function autoScanSet() {
    var x = document.getElementById("auto_check").checked;
    //var y = document.getElementsByName("auto_name").value;
    //document.getElementById("demo").checked = true
    //alert(x)
    //alert(y)
    if (x == true){
        document.getElementById("time-scan").style.display = "block";
    }
    else{
        document.getElementById("time-scan").style.display = "none";
    }
}

function getInternetType() {
    var x = document.getElementById("internet").value;
    // document.getElementById("demo").innerHTML = x;
    if (x == "lan"){
        document.getElementById("select-wifi").style.display = "none";
        document.getElementById("select-cellular").style.display = "none";
    }
    else if (x == "wifi"){
        document.getElementById("select-wifi").style.display = "block";
        document.getElementById("select-cellular").style.display = "none";
    }
    else{
        document.getElementById("select-wifi").style.display = "none";
        document.getElementById("select-cellular").style.display = "block";
    }

 }

function getConnectionType() {
    var y = document.getElementById("connection").value;
    // document.getElementById("demo").innerHTML = x;
    if (y == "ssh"){
        document.getElementById("select-tcp").style.display = "none";
    }
    else{
        document.getElementById("select-tcp").style.display = "block";
    }
}

function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function refreshpage(){
    alert("the page will refresh after 10 second")
    location.reload();
}

// setTimeout(refreshpage,10000)

