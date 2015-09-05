<!DOCTYPE html>
<html>
   <head>
     <link href="/static/css/style.css" rel="stylesheet">
     <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
   </head>
   <body>
     <input type="text" name="link" />
     <button id="add_link">Add a link!</button>
     <div id="links">
      % for link in links:
        <div id="wrapper_link_{{link[0]}}">
          <p id="link_{{ link[0] }}">{{link[1]}}</p>
            <p>
              <input type="text" value="{{link[1]}}" id="link_edit_form_id_{{ link[0] }}" />
              <button class="edit" id="link_edit_id_{{ link[0] }}">Edit</button>
              <button class="delete" id="link_delete_id_{{ link[0] }}">Delete</button>
          </p>
        </div>
      % end
     </div>
     <script type="text/javascript">
       $(document).on("click", "#add_link", function(e) {
         $.post("/add/link", {"link": $("input[name='link']").val()})
          .done(function(string) {
             $("#links").html($("#links").html() + string);
             // TODO: Hide edit field when displaying the new link.
          });
         e.preventDefault();
       });

       $(document).on("click", ".edit", function(e) {
          var link_id = $(this).attr('id').replace('link_edit_id_','');
          var new_link = $("#link_edit_form_id_" + link_id).val();
          $.ajax({
             type: "PUT",
             url: "/edit/link/" + link_id,
             data: {"link": new_link}
          })
          .done(function() {
            $("#link_" + link_id).html(new_link);
          });
          e.preventDefault();
       });

       $(document).on("click", ".delete", function(e) {
        var link_id = $(this).attr('id').replace('link_delete_id_','');
         $.ajax({
            type: "DELETE",
            url: "/delete/link/" + link_id
         })
         .done(function() {
            $("#wrapper_link_" + link_id).remove();
         });
         e.preventDefault();
       });
     </script>
   </body>
</html>