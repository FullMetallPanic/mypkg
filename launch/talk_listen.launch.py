import launch
import launch.actions
import launch_ros.actions

def generate_launch_description():

    dealer_node = launch_ros.actions.Node(
        package='mypkg',
        executable='dealer',  
        output='screen',
    )

    
    judge_node = launch_ros.actions.Node(
        package='mypkg',
        executable='judge',  
        output='screen',
    )


    listener_node = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen',
    )

    return launch.LaunchDescription([
        dealer_node,
        judge_node,
        listener_node,
    ])
