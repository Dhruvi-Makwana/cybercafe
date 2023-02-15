$(document).ready(function()
{
    configDataTable("#system_data", '/getdata/', [
            { data: 'name__name',title:'Name' },
            { data: 'name__company',title:'Company' },
            { data: 'name__ram',title:'RAM' },
            { data: 'name__unit',title:'Unit' },
            { data: 'status',title:'Status'},

        ],
    )
    $('#system_data tfoot th').each( function () {
    var title = $('#system_data tfoot th').eq( $(this).index() ).text();
//    $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
} );


// DataTable
// var table1 = $('#system_data').DataTable();
//  table1.columns().eq( 0 ).each( function ( colIdx ) {
//         $( 'input', table1.column( colIdx ).footer() ).on( 'keyup change', function ()
//         {
//         table1 .column( colIdx ) .search( this.value ).draw();
//         } );
//   $(document).ready(function()
// {
//     configDataTable("#system_data", '/getdata/', [
//             { data: 'name__name',title:'Name' },
//             { data: 'name__company',title:'Company' },
//             { data: 'name__ram',title:'RAM' },
//             { data: 'name__unit',title:'Unit' },
//             { data: 'status',title:'Status'},

//         ],
//     )
//     $('#system_data tfoot th').each( function () {
//     var title = $('#system_data tfoot th').eq( $(this).index() ).text();
// //    $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
// } );


// DataTable
var table1 = $('#system_data').DataTable();
 table1.columns().eq( 0 ).each( function ( colIdx ) {
        $( 'input', table1.column( colIdx ).footer() ).on( 'keyup change', function ()
        {
        table1 .column( colIdx ) .search( this.value ).draw();
        } );
        } );
        } );
