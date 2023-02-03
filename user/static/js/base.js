function configDataTable(id, url, columns)
{
   $(id).DataTable
 ({
      searchBuilder: {
            enterSearch: true
             },

    "serverSide": true,
    "processing": true,
    "pageLength": 10,
    "lengthChange" : true,
    "order": [0, "asc"],

        ajax: {
                url: url,
                dataSrc: 'data'

               },
      columns: columns,
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