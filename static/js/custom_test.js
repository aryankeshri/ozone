<script type="text/javascript" >
    $(document).ready(function(){
        $('select[name=league]').change(function(){

            league_id = $(this).val();
            request_url = '/admin/get_team/' + id_league + '/';
            $.ajax({
                url: request_url,
                success: function(data){
                console.log(data);
                    $.each(data, function(key, value){
                        $('select[name=team]').append('<option value="' + this.key + '">' + this.value +'</option>');
                    });
                }
                return false;
            })
        })
    });
</script>

<script>
  $( function() {
    var dateFormat = "mm/dd/yy",
      from = $( "#id_start_date" )
        .datepicker({
          defaultDate: "+1w",
          changeMonth: true,
          numberOfMonths: 3
        })
        .on( "change", function() {
          to.datepicker( "option", "minDate", getDate( this ) );
        }),
      to = $( "#id_end_date" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3
      })
      .on( "change", function() {
        from.datepicker( "option", "maxDate", getDate( this ) );
      });

    function getDate( element ) {
      var date;
      try {
        date = $.datepicker.parseDate( dateFormat, element.value );
      } catch( error ) {
        date = null;
      }

      return date;
    }
  } );
</script>