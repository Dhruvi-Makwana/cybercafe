
$(document).ready(function()
{
 configDataTable("#display_user", '/get-userdata/',
         [
             {data:'id',title:''},
            { data: 'first_name',title:'First Name' },
            { data: 'last_name',title:'Last Name' },
            { data: 'mobile_number',title:'Mobile Number' },
        ],

    )
    // Setup - add a text input to each footer cell
$('#display_user tfoot th').each( function () {
var title = $('#display_user thead th').eq( $(this).index() ).text();
$(this).html( '<input type="text" placeholder="Search '+title+'" />' );
} );

var user_table = $('#display_user').DataTable();

 user_table.columns().eq( 0 ).each( function ( colIdx )
  { $( 'input', user_table.column( colIdx ).footer() ).on( 'keyup change', function ()
   { user_table.column( colIdx ) .search( this.value ).draw();
  } );
  } );
  } );