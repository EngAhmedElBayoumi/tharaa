

$(document).ready(function() {
    var $broker_company_select = $("#broker_company_select");
    var $broker_company_input = $("#broker_company_input");

    $broker_company_select.on("change", function() {
        var selectedValue = $(this).val();
        console.log('select', selectedValue);
        $broker_company_input.val(selectedValue);
    });




    var $dev_sales_select = $("#dev_sales_select");
    var $dev_sales_input = $("#dev_sales_input");

    $dev_sales_select.on("change", function() {
        var selectedValue = $(this).val();
        console.log('select', selectedValue);
        $dev_sales_input.val(selectedValue);
    });

// add event lisenter on the select element
$dev_sales_select.on("change", function() {
    var selectedValue = $(this).val();
    $dev_sales_input.val(selectedValue);

    // // ajax call to get Dev Sales Manager depend on dev sales and update dev_sales_manager input
    // var dev_sales_manager_input=document.getElementById("dev_sales_manager")
    // $.ajax({
    //     url: '/home/get_dev_sales_manager',
    //     type: 'GET',
    //     data: {
    //         'dev_sales': selectedValue
    //     },
    //     success: function(response) {
    //         // set the value of the input element
    //         dev_sales_manager_input.value = response;
    //     },
    //     error: function(xhr, status, error) {
    //         console.error(error);
    //     }
    // });
    




})



});
