<!DOCTYPE html>
<html>
   <head>
     <link href="/static/css/style.css" rel="stylesheet">
     <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
     <script type="text/javascript">
       $(document).ready(function() {

         $("#add_link").click(function(e) {
           $.post("/add/link", {"link": $("input[name='link']").val()})
            .done(function(string) {
               $("#links").html($("#links").html() + string);
            });
           e.preventDefault();
         });

         $(".edit").click(function(e) {
           $.ajax({
              type: "PUT",
              url: "/edit/link",
              data: {"edit_link": $(this).attr('id').replace('link_edit_id_','')}
           })
           .done(function() {
              alert("Replaced!");
           });
           e.preventDefault();
         });

         $(".delete").click(function(e) {
           $.ajax({
              type: "DELETE",
              url: "/delete/link/" + $(this).attr('id').replace('link_delete_id_','')
           })
           .done(function() {
              $(this).hide();
           });
           e.preventDefault();
         });

       });
     </script>
   </head>
   <body>
     <input type="text" name="url" />
     <button id="add_link">Add a link!</button>
     <div id="links">
     </div>
   </body>
</html>