$('#PContainer').scroll(function() { 
    $('#FixedDiv').css('top', $(this).scrollTop());
});