<!DOCTYPE html>
<html>
   <head>
     <link href="/static/css/style.css" rel="stylesheet">
     <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
     <style type="text/css">
     .green{
      background-color: green;
      }</style>
   </head>
   <body>
     <input type="text" name="entry" />
     <button id="add_entry">Add an entry!</button>
     <div id="notepad">
      % for entry in notepad:
        <div id="wrapper_entry_{{entry[0]}}"
        % if entry[2] == 1:
          class="green"
        % end
        >
          <p id="entry_{{ entry[0] }}">{{entry[1]}}</p>
            <p>
              <input type="text" value="{{entry[1]}}" id="entry_edit_form_id_{{ entry[0] }}" />
              <button class="edit" id="entry_edit_id_{{ entry[0] }}">Edit</button>
              <button
              % if entry[2] == 1:
                  class="open"
                % else:
                  class="close"
                % end
               id="entry_close_id_{{ entry[0] }}">
                % if entry[2] == 1:
                  Open
                % else:
                  Close
                % end
              </button>
              <button class="delete" id="entry_delete_id_{{ entry[0] }}">Delete</button>
          </p>
        </div>
      % end
     </div>
     <script type="text/javascript">
       $(document).on("click", "#add_entry", function(e) {
         $.post("/notepad/add/entry", {"entry": $("input[name='entry']").val()})
          .done(function(string) {
             $("#notepad").html($("#notepad").html() + string);
             // TODO: Hide edit field when displaying the new entry.
          });
         e.preventDefault();
       });

       $(document).on("click", ".edit", function(e) {
          var entry_id = $(this).attr('id').replace('entry_edit_id_','');
          var new_entry = $("#entry_edit_form_id_" + entry_id).val();
          $.ajax({
             type: "PUT",
             url: "/notepad/edit/entry/" + entry_id,
             data: {"entry": new_entry}
          })
          .done(function() {
            $("#entry_" + entry_id).html(new_entry);
          });
          e.preventDefault();
       });

       $(document).on("click", ".close", function(e) {
          var entry_id = $(this).attr('id').replace('entry_close_id_','');
          var new_entry = $("#entry_close_form_id_" + entry_id).val();
          $.ajax({
             type: "PUT",
             url: "/notepad/close/entry/" + entry_id,
          })
          .done(function() {
            $("#wrapper_entry_" + entry_id).addClass("green");
            $("#entry_close_id_" + entry_id).removeClass();
            $("#entry_close_id_" + entry_id).addClass("open");
            $("#entry_close_id_" + entry_id).html("Open");
          });
          e.preventDefault();
       });

       $(document).on("click", ".open", function(e) {
          var entry_id = $(this).attr('id').replace('entry_close_id_','');
          var new_entry = $("#entry_close_form_id_" + entry_id).val();
          $.ajax({
             type: "PUT",
             url: "/notepad/open/entry/" + entry_id,
          })
          .done(function() {
            $("#wrapper_entry_" + entry_id).removeClass("green");
            $("#entry_close_id_" + entry_id).removeClass();
            $("#entry_close_id_" + entry_id).addClass("close");
            $("#entry_close_id_" + entry_id).html("Close");
          });
          e.preventDefault();
       });

       $(document).on("click", ".delete", function(e) {
        var entry_id = $(this).attr('id').replace('entry_delete_id_','');
         $.ajax({
            type: "DELETE",
            url: "/notepad/delete/entry/" + entry_id
         })
         .done(function() {
            $("#wrapper_entry_" + entry_id).remove();
         });
         e.preventDefault();
       });
     </script>
   </body>
</html>