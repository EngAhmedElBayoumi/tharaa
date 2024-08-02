// after document load
$(document).ready(function() {
    // get element by class export_link , import_link
    var export_link = document.getElementsByClassName("export_link");
    var import_link = document.getElementsByClassName("import_link");
    // change style to be button by css code 
    export_link[0].style = "background-color: #32CD32; color: white; margin-top:10px; margin-bottom:10px; display: flex; justify-content: center; align-items: center; font-size: 24px;";
    import_link[0].style = "background-color: #32CD32; color: white; margin-top:10px; margin-bottom:10px; display: flex; justify-content: center; align-items: center; font-size: 24px;";  
});