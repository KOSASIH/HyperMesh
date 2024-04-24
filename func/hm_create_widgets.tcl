# hm_create_widgets.tcl

# Load necessary packages
package require Tcl 8.4
package require HyperMesh

# Define a procedure to create a custom widget
proc create_widget {} {
    # Create a new window
    set window_name [window_create -title "Custom Widget" -width 500 -height 300]

    # Add a label to the window
    set label_name [label_create -parent $window_name -text "Welcome to the Custom Widget!"]

    # Add a button to the window
    set button_name [button_create -parent $window_name -text "Close Widget" -command {window_destroy $window_name}]

    # Add a text box to the window
    set text_box_name [text_create -parent $window_name -width 40 -height 10]

    # Add a dropdown menu to the window
    set menu_name [menu_create]
    menu_add_command -menu $menu_name -text "Option 1" -command {puts "Option 1 selected"}
    menu_add_command -menu $menu_name -text "Option 2" -command {puts "Option 2 selected"}
    set dropdown_name [dropdown_create -parent $window_name -menu $menu_name -text "Select an option"]

    # Add a checkbox to the window
    set checkbox_name [checkbox_create -parent $window_name -text "Checkbox"]

    # Add a radio button group to the window
    set radio_button_group_name [radio_button_group_create -parent $window_name]
    radio_button_group_add_button -name $radio_button_group_name -text "Radio Button 1"
    radio_button_group_add_button -name $radio_button_group_name -text "Radio Button 2"

    # Add a progress bar to the window
    set progress_bar_name [progress_bar_create -parent $window_name -mode "determinate" -value 50]

    # Add a slider to the window
    set slider_name [slider_create -parent $window_name -from 0 -to 100 -value 50]

    # Add a tree view to the window
    set tree_view_name [tree_view_create -parent $window_name -columns "Column 1" "Column 2"]
    tree_view_insert_item -name $tree_view_name -text "Item 1" -values "Value 1" "Value 2"
    tree_view_insert_item -name $tree_view_name -text "Item 2" -values "Value 3" "Value 4"

    # Add a table view to the window
    set table_view_name [table_view_create -parent $window_name -columns "Column 1" "Column 2"]
    table_view_insert_row -name $table_view_name -values "Value 1" "Value 2"
    table_view_insert_row -name $table_view_name -values "Value 3" "Value 4"

    # Add a canvas to the window
    set canvas_name [canvas_create -parent $window_name -width 200 -height 200]
    canvas_create_rectangle -name $canvas_name -x 50 -y 50 -width 100 -height 100 -fill "red"

    # Add a hyperlink to the window
    set hyperlink_name [hyperlink_create -parent $window_name -text "Click here" -url "https://www.example.com"]

    # Add a tooltip to the window
    set tooltip_name [tooltip_create -parent $window_name -text "This is a tooltip"]

    # Add a status bar to the window
    set status_bar_name [status_bar_create -parent $window_name]

    # Add a menu bar to the window
    set menu_bar_name [menu_bar_create -parent $window_name]
    menu_bar_add_menu -name $menu_bar_name -text "File"
    menu_bar_add_menu_item -name $menu_bar_name -text "New" -command {puts "New file"}
    menu_bar_add_menu_item -name $menu_bar_name -text "Open" -command {puts "Open file"}
    menu_bar_add_menu_item -name $menu_bar_name -text "Save" -command {puts "Save file"}
    menu_bar_add_menu_item -name $menu_bar_name -text "Exit" -command {window_destroy $window_name}

    # Show the window
    window_show $window_name
}

# Call the procedure to create the custom widget
create_widget
