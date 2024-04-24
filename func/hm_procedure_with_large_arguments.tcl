# hm_procedure_with_large_arguments.tcl

# This procedure demonstrates the use of large arguments in a HyperMesh Tcl script.

# Input arguments:
# $1 - The first argument, a string containing a message to display.
# $2 - The second argument, an integer representing the number of times to repeat the message.
# $3 - The third argument, a list of colors to use for the message text.
# $4 - The fourth argument, a dictionary containing additional options for the procedure.

proc procedure_with_large_arguments {args} {
    # Extract the input arguments.
    set message [lindex $args 0]
    set repeat_count [lindex $args 1]
    set colors [lindex $args 2]
    set options [lindex $args 3]

    # Initialize variables.
    set i 0
    set text_color "black"

    # Check the options dictionary for additional settings.
    if {[info exists options(-bold)]} {
        set text_color "red"
    }

    # Display the message the specified number of times.
    for {set i 0} {$i < $repeat_count} {incr i} {
        # Choose a random color from the list of colors.
        set random_color [lindex $colors [expr {int(rand() * [llength $colors])}]]

        # Display the message with the chosen color.
        puts "Message $i: [format $message $i] [color $random_color]$message $i[color black]"
    }
}

# Example usage:
# hm_procedure_with_large_arguments "The message is: %d" 5 (red green blue) {-bold 1}
