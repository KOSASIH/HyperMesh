# hm_run_batch_mode.tcl

# Load necessary packages
package require Tcl 8.4
package require HyperMesh

# Define a procedure to run HyperMesh in batch mode
proc run_batch_mode {} {
    # Set the batch mode flag
    set batch_mode_flag 1

    # Load the necessary modules
    load_module -name "hm_get_entity_id"
    load_module -name "hm_list_assemblies"
    load_module -name "hm_get_component_info"
    load_module -name "hm_query_database"
    load_module -name "hm_create_window"
    load_module -name "hm_create_widgets"

    # Run the necessary commands
    hm_get_entity_id -entity_type "NODE" -entity_name "N1"
    hm_list_assemblies
    hm_get_component_info -component_name "C1"
    hm_query_database -query "SELECT * FROM TABLE1"
    hm_create_window -window_name "Custom Window" -width 500 -height 300
    hm_create_widget -widget_name "Custom Widget" -label_text "Welcome to the Custom Widget!" -button_text "Close Widget" -text_box_width 40 -text_box_height 10 -menu_text "Select an option" -checkbox_text "Checkbox" -radio_button_group_name "Radio Button Group" -progress_bar_mode "determinate" -progress_bar_value 50 -slider_from 0 -slider_to 100 -slider_value 50 -tree_view_columns "Column 1" "Column 2" -table_view_columns "Column 1" "Column 2" -canvas_width 200 -canvas_height 200 -hyperlink_text "Click here" -hyperlink_url "https://www.example.com" -tooltip_text "This is a tooltip" -status_bar_text "Ready" -menu_text "File" -menu_commands "New Open Save Exit"
}

# Call the procedure to run HyperMesh in batch mode
run_batch_mode
