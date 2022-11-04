INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_HMAC HMAC)

FIND_PATH(
    HMAC_INCLUDE_DIRS
    NAMES HMAC/api.h
    HINTS $ENV{HMAC_DIR}/include
        ${PC_HMAC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    HMAC_LIBRARIES
    NAMES gnuradio-HMAC
    HINTS $ENV{HMAC_DIR}/lib
        ${PC_HMAC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/HMACTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(HMAC DEFAULT_MSG HMAC_LIBRARIES HMAC_INCLUDE_DIRS)
MARK_AS_ADVANCED(HMAC_LIBRARIES HMAC_INCLUDE_DIRS)
