# CMake generated Testfile for 
# Source directory: /home/christian/gr-HMAC/python
# Build directory: /home/christian/gr-HMAC/build/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(qa_HMAC_append "/usr/bin/sh" "/home/christian/gr-HMAC/build/python/qa_HMAC_append_test.sh")
set_tests_properties(qa_HMAC_append PROPERTIES  _BACKTRACE_TRIPLES "/usr/lib/x86_64-linux-gnu/cmake/gnuradio/GrTest.cmake;122;add_test;/home/christian/gr-HMAC/python/CMakeLists.txt;46;GR_ADD_TEST;/home/christian/gr-HMAC/python/CMakeLists.txt;0;")
add_test(qa_HMAC_verify "/usr/bin/sh" "/home/christian/gr-HMAC/build/python/qa_HMAC_verify_test.sh")
set_tests_properties(qa_HMAC_verify PROPERTIES  _BACKTRACE_TRIPLES "/usr/lib/x86_64-linux-gnu/cmake/gnuradio/GrTest.cmake;122;add_test;/home/christian/gr-HMAC/python/CMakeLists.txt;47;GR_ADD_TEST;/home/christian/gr-HMAC/python/CMakeLists.txt;0;")
