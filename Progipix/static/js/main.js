$(function () {
    //Initialize Select2 Elements
    $(".select2").select2();
});


function open_modal(url) {
    $("#modall").load(url, function () {
        $(this).modal("show");
    });
  }

  function close_modal(){
    $('#modall').modal('hide');
  }

  function Success(message) {
    Swal.fire({
        title: "Good job",
        text: message,
        icon: "success",
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 1200
    }).then(function(){
      location.reload();
    });
}
  
  $(document).on('submit', '#formajax', function(event){
    event.preventDefault();
    $.ajax({
      data: $('#formajax').serialize(),
      url: $('#formajax').attr('action'),
      type: $('#formajax').attr('method'),
      dataType: 'json',
      headers: {'X-Requested-With': 'XMLHttpRequest'},
      success: function (response) {
        Success(response.message);
        close_modal();
      }
    })
  });