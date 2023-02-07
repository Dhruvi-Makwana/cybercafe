function configDataTable(id, url)
{
   $(id).DataTable
 ({
      searchBuilder: {
            enterSearch: true
             },

    "serverSide": true,
    "processing": true,
    "pageLength": 10,

    "order": [0, "asc"],

        ajax: {
                url: url,
                dataSrc: 'data'

               },
      
      'columnDefs': [{
         'targets': 0,
         'searchable': false,
         'orderable': false,
         'className': 'dt-body-center',
         'render': function (data, type, full, meta){
             return '<input type="checkbox" name="id[]" value="' + $('<div/>').text(data).html() + '">';
         }
      }],

 });

}

function getAjax(url, callback=null){

    $.ajax({
        type:'GET',
        url: url,
            dataType: 'json',
            dataSrc: 'data',
            success:function (data){
                if(callback){
                    callback(data.data)
                }
        },
        });



}




//    ajax: function ( data, callback, settings ) {
//            var out = [];
//            for ( var i=data.start, ien=data.start+data.length ; i<ien ; i++ ) {
//                out.push( );
//            }
//
//            setTimeout( function () {
//                callback( {
//                    draw: data.draw,
//                    data: out,
//                    recordsTotal: 5000000,
//                    recordsFiltered: 5000000
//                } );
//            }, 50 );
//        },
//
//    } );