/**
 * \file legion_defines.h
 * Public-facing definitions of variables configured at build time
 * DO NOT EDIT THIS FILE WITHOUT CHANGING runtime.mk ALSO
 */

/********************** IMPORTANT **************************
 *
 * This file is PURE C, **NOT** C++. Keep any C++-isms in
 * legion_types.h, or elsewhere.
 *
 ******************** IMPORTANT ****************************/

/* #undef DEBUG_LEGION */

/* #undef LEGION_PRIVILEGE_CHECKS */

/* #undef LEGION_BOUNDS_CHECKS */

#define LEGION_MAX_DIM 4

/* #undef LEGION_MAX_FIELDS */

#define LEGION_USE_CUDA

/* #undef LEGION_GPU_REDUCTIONS */

#define LEGION_USE_ZLIB

/* #undef LEGION_REDOP_COMPLEX */

/* #undef LEGION_REDOP_HALF */

/* #undef LEGION_WARNINGS_FATAL */

/* #undef LEGION_USE_HDF5 */

/* #undef LEGION_SPY */

#define LEGION_USE_LIBDL
