# CMake generated Testfile for 
# Source directory: /home/kali/SNS_Project/YesWeCAN/Hazelnet
# Build directory: /home/kali/SNS_Project/YesWeCAN/Hazelnet
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_hzl_client_desktop "/home/kali/SNS_Project/YesWeCAN/Hazelnet/test_hzl_client_desktop")
set_tests_properties(test_hzl_client_desktop PROPERTIES  _BACKTRACE_TRIPLES "/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;417;add_test;/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;0;")
add_test(test_hzl_client_desktop_shared "/home/kali/SNS_Project/YesWeCAN/Hazelnet/test_hzl_client_desktop_shared")
set_tests_properties(test_hzl_client_desktop_shared PROPERTIES  _BACKTRACE_TRIPLES "/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;419;add_test;/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;0;")
add_test(test_hzl_server_desktop "/home/kali/SNS_Project/YesWeCAN/Hazelnet/test_hzl_server_desktop")
set_tests_properties(test_hzl_server_desktop PROPERTIES  _BACKTRACE_TRIPLES "/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;498;add_test;/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;0;")
add_test(test_hzl_server_desktop_shared "/home/kali/SNS_Project/YesWeCAN/Hazelnet/test_hzl_server_desktop_shared")
set_tests_properties(test_hzl_server_desktop_shared PROPERTIES  _BACKTRACE_TRIPLES "/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;500;add_test;/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;0;")
add_test(test_hzl_interop_desktop "/home/kali/SNS_Project/YesWeCAN/Hazelnet/test_hzl_interop_desktop")
set_tests_properties(test_hzl_interop_desktop PROPERTIES  _BACKTRACE_TRIPLES "/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;556;add_test;/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;0;")
add_test(test_hzl_interop_desktop_shared "/home/kali/SNS_Project/YesWeCAN/Hazelnet/test_hzl_interop_desktop_shared")
set_tests_properties(test_hzl_interop_desktop_shared PROPERTIES  _BACKTRACE_TRIPLES "/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;558;add_test;/home/kali/SNS_Project/YesWeCAN/Hazelnet/CMakeLists.txt;0;")
subdirs("external/libascon")
