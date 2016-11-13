######################################################################################
# Packages needed for examples
######################################################################################

# These examples have no external dependencies and should always build.
add_executable(freenect-wavrecord wavrecord.c)
target_link_libraries(freenect-wavrecord freenect)
install(TARGETS freenect-wavrecord
        DESTINATION bin)
