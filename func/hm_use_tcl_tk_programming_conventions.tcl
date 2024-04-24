# Load the HyperMesh Tcl/Tk library
package require HyperMesh

# Create a namespace for mesh-related procedures
namespace eval hm_mesh {

    # Procedure to create a new HyperMesh model
    proc create_new_model {model_name} {
        # Check if the model name is valid
        if {$model_name == ""} {
            puts "Error: Model name cannot be empty."
            return
        }

        # Create a new HyperMesh model
        HM_NewModel $model_name

        # Print a success message
        puts "Successfully created new model: $model_name"
    }

    # Procedure to add a box entity to a HyperMesh model
    proc add_box_entity {model_name x_coord y_coord z_coord length width height} {
        # Check if the model name is valid
        if {$model_name == ""} {
            puts "Error: Model name cannot be empty."
            return
        }

        # Check if the coordinates and dimensions are valid
        if {($x_coord == "") || ($y_coord == "") || ($z_coord == "") || ($length == "") || ($width == "") || ($height == "")} {
            puts "Error: Coordinates and dimensions cannot be empty."
            return
        }

        # Add a box entity to the HyperMesh model
        HM_AddBoxEntity $model_name $x_coord $y_coord $z_coord $length $width $height

        # Print a success message
        puts "Successfully added box entity to model: $model_name"
    }

}
