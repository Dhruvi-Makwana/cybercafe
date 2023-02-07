// function configDataTable(id, url, columns)
// {
//    $(id).DataTable
//  ({
//       searchBuilder: {
//             enterSearch: true
//              },

//     "serverSide": true,
//     "processing": true,
//     "pageLength": 10,

//     "order": [0, "asc"],

//         ajax: {
//                 url: url,
//                 dataSrc: 'data'

//                },
//       columns: columns,
//       'columnDefs': [{
//          'targets': 0,
//          'searchable': false,
//          'orderable': false,
//          'className': 'dt-body-center',
//          'render': function (data, type, full, meta){
//              return '<input type="checkbox" name="id[]" value="' + $('<div/>').text(data).html() + '">';
//          }
//       }],

//  });

// }

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