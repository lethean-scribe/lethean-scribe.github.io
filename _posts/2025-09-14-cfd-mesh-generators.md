---
layout: post
title: "CFD mesh generators"
date: Sun Sep 14 8:00:00 AUSEST 2025
categories: [CFD, Mesh, Gasdynamics]
tags: [CFD, Mesh, Gasdynamics]
author: Lethean Scribe
excerpt: Review of mesh generators
mathjax: true
---

* content
{:toc}

In this post we will review commercial and open-source CFD mesh generators.
This comprehensive table contains 150+ mesh generation software packages categorized by type, capabilities, licensing, and developers.

# CFD Mesh Generation Software Codes - Features Comparison

| Software Name | Category | Dimensions | Element Types | Key Features | License | Developer/Company |
|--------------|----------|------------|---------------|--------------|---------|-------------------|
| **ADMesh** | STL Processing | 3D | Triangular | Processing triangulated solid meshes in STL format | Public Domain | Anthony D. Martin |
| **ANGENER** | Triangular Mesh | 2D | Triangular | Anisotropic mesh adaptation | Public Domain | Vit Dolejsi |
| **AUTOMESH2D** | Quadrilateral Mesh | 2D | Quadrilateral | Automatic adaptive quad mesh generator for metal forming | Public Domain | Shandong University |
| **CAMINO** | Octree/Quadtree | 2D/3D | Triangular/Tetrahedral | Generalized octree/quadtree approach | Public Domain | Tao Chen |
| **Cart3D** | Cartesian Mesh | 3D | Hexahedral | Pre-processing tools for cartesian mesh generation | Public Domain | Michael J. Aftosmis |
| **CGAL** | Computational Geometry | 2D/3D | Triangular/Tetrahedral | Various packages for triangle and tetrahedral mesh generation | Dual License | CGAL |
| **CGM** | Geometry Library | 3D | Various | Geometry functionality for mesh generation | Public Domain | Tim Tautges |
| **Chimera Grid Tools** | Overset Grid | 3D | Structured | Tools for Chimera overset grid approach | Public Domain | William M. Chan |
| **COG 2.0** | Delaunay Grid | 2D/3D | Triangular/Tetrahedral | Delaunay grids with few nodes for complex geometries | Partially Public Domain | Ilja Schmelzer |
| **CQMesh** | Quadrilateral Mesh | 2D | Quadrilateral | Convex quadrilateral meshes of arbitrary polygonal domains | Public Domain | Marcelo Siqueira |
| **CSCMDO** | Multi-block Grid | 3D | Structured | Multi-block volume grid generator for optimization | Public Domain | Bill Jones |
| **CUBIT** | Finite Element Mesh | 2D/3D | Quadrilateral/Hexahedral | Robust unattended mesh generation | Commercial | SANDIA, BYU |
| **delaundo** | Delaunay Mesh | 2D | Triangular | High quality triangular grids | Public Domain | Jens-Dominik Müller |
| **DelIso** | Iso-surface Mesh | 3D | Triangular | Mesh Iso-surface from volume data with Delaunay triangles | Public Domain | Tamal K. Dey |
| **Delos** | Surface Mesh | 2D | Triangular | Automatic 2D mesh generator for almost flat surfaces | Public Domain | Olivier Stab |
| **DelPSC** | Delaunay Mesh | 3D | Tetrahedral | Quality Delaunay mesh for 3D domains | Public Domain | Tamal K. Dey |
| **DIAMESH** | General Mesh | 2D/3D | Triangular/Tetrahedral | 2D triangular, 3D tet meshing and surface remeshing | Public Domain | Alain Rassineux |
| **Discretizer** | Block-structured | 3D | Structured | Interactive mesh creation for CFD applications | Public Domain | Björn Bergqvist |
| **DistMesh** | MATLAB Mesh | 2D/3D | Triangular/Tetrahedral | Simple MATLAB code for unstructured meshes | Public Domain | Per-Olof Persson |
| **enGrid** | Tetrahedral Grid | 3D | Tetrahedral | Grid generation with prismatic boundary layers | Public Domain | enGits |
| **EZ4U** | Quadrilateral Mesh | 2D | Quadrilateral | Unstructured mesh generation with GUI | Public Domain | LACAN |
| **felicity** | Unstructured Mesh | 2D/3D | Triangular/Tetrahedral | Algorithm with guaranteed angle bounds | Public Domain | Shawn Walker |
| **femmesh** | Finite Element | 2D | Triangular | Interactive 2D FEM mesh generation | Public Domain | Medical Physics, UCL |
| **FIST** | Polygon Triangulation | 2D/3D | Triangular/Quadrilateral | Robust polygon triangulation (ear clipping) | Public Domain | Martin Held |
| **GENIE++** | Structured Grid | 3D | Structured | Multi-block grids for internal-external flow | Public Domain | Bharat Soni |
| **Geompack++** | Finite Element | 2D/3D | Triangular/Quadrilateral/Tetrahedral | Comprehensive software package for FE mesh generation | Public Domain | Barry Joe |
| **Globegen** | Prismatic Grid | 3D | Prismatic | Unstructured prismatic grid generator for global meshes | Public Domain | Nash'at Ahmad |
| **GMSH** | Delaunay-based | 2D/3D | Triangular/Tetrahedral | Adapted meshes for lines, surfaces and volumes | Public Domain | Jean-Francois Remacle, Christophe Geuzaine |
| **GNU Triangulated Surface** | Surface Library | 3D | Triangular | 2D Delaunay and constrained Delaunay triangulation | Open Source | SourceForge |
| **GrAL** | Grid Library | Various | Various | Generic library for grid data structures | Public Domain | Guntram Berti |
| **GridEx** | Interactive Mesh | 3D | Various | Interactive software with CAD geometry access | Public Domain | GEOLAB |
| **GRIDGEN** | Structured Grid | 3D | Structured | Multiple block structured grids with GUI | Public Domain | NASA |
| **gridgen** | Orthogonal Grid | 2D | Orthogonal | Orthogonal grid generator based on CRDT algorithm | Public Domain | Pavel Sakov |
| **Gridgen** | Ocean Grid | 2D | Orthogonal | MATLAB-based tool for ocean circulation models | Public Domain | USGS |
| **gridpak** | Coastal Grid | 2D | Orthogonal | 2D orthogonal grid generation for coastal engineering | Public Domain | IMCS |
| **GridTool** | Surface Modeling | 3D | Various | Surface modeling and grid generation tool | Public Domain | NASA Langley |
| **GRUMMP** | Mixed-element | 2D/3D | Various | Quality generation and refinement of mixed-element meshes | Public Domain | ANSLab |
| **GTS** | Triangulated Surface | 3D | Triangular | GNU Triangulated Surface Library | Open Source | SourceForge |
| **Gudhi** | Computational Topology | Various | Various | Library for Computational Topology and TDA | Open Source | INRIA |
| **G3D** | Groundwater Grid | 3D | Structured | 3D grids for groundwater simulations | Public Domain | IMI |
| **HypGrid** | Hyperbolic Grid | 2D/3D | Orthogonal | Grid generator based on hyperbolic equations | Public Domain | Riso Wind Energy Department |
| **IMTEK Mathematica** | Interface | Various | Various | Mathematica interface to various mesh generators | Public Domain | Freiburg Chair for Simulation |
| **iso2mesh** | Medical Mesh | 3D | Tetrahedral | MATLAB toolbox for medical image meshing | Public Domain | - |
| **JMesh** | Minimal Surfaces | 3D | Triangular | Approximations of minimal surfaces | Public Domain | James T. Hoffman |
| **LaGriT** | Unstructured Grid | 3D | Tetrahedral | Grid generation and optimization for 3D moving surfaces | Public Domain | Los Alamos National Laboratory |
| **LBG** | Layer-based | 3D | Structured | Layer based 3D structured grid generator | Public Domain | WIAS |
| **LBIE-Mesher** | Level Set Mesh | 2D/3D | Various | Adaptive meshing from volumetric imaging data | Public Domain | Austin CCV |
| **MAdLib** | Mesh Adaptation | 2D/3D | Triangular/Tetrahedral | Global node repositioning and mesh adaptation | Open Source | Gaëtan Compère |
| **MAKROS-A** | Surface Meshing | 3D | Quadrilateral | Quadrilateral surface meshing for AutoCad data | Public Domain | Guenther Boege |
| **Méfisto-maillages** | General Mesh | 2D/3D | Various | Structured/unstructured generation of 2D/3D meshes | Public Domain | Alain Perronnet |
| **MegaCads** | Multiblock Elliptic | 2D/3D | Structured | Multiblock elliptic grid generation and CAD system | Public Domain | DLR Institute for Design Aerodynamics |
| **Meshing tools** | Viewing/Processing | 3D | Various | Interactive 3D viewing and mesh manipulation | Public Domain | Pascal Frey |
| **MeshLab** | Mesh Processing | 3D | Triangular | Processing and editing of unstructured 3D triangular meshes | Open Source | - |
| **Mesh Maker Pro** | 3D Modeling | 3D | Various | Tool for creating 3D models for graphics programming | Public Domain | Dan Keller |
| **Mesh2D** | Adaptive Triangular | 2D | Triangular | Adaptive triangular mesh generator for unstructured CFD | Public Domain | Francis X. Giraldo |
| **MeshGenC++** | Unstructured Mesh | 2D/3D | Triangular/Tetrahedral | Package for generating unstructured meshes | Public Domain | James Rossmanith |
| **MESQUITE** | Mesh Quality | Various | Various | Library for improving mesh quality | Public Domain | TSTT |
| **MG** | Finite Element | 2D/3D | Various | 3D finite element meshes with interactive graphics | Public Domain | Luiz Cristovao Gomes Coelho |
| **MMG** | Mesh Adaptation | 2D/3D | Triangular/Tetrahedral | Surface and volume mesh adaptation | Open Source | MMG Open Source Consortium |
| **NETGEN** | CSG Mesh | 2D/3D | Triangular/Tetrahedral | Mesh generator for CSG geometries | Public Domain | Joachim Schöberl |
| **MMESH3d** | Semi-structured | 2D/3D | Hexahedral/Prismatic | Semi-structured multiblock mesh generator | Public Domain | Simone Marras |
| **NWGrid** | Hybrid Grid | 2D/3D | Various | Automated grid generation with time-dependent adaptivity | Public Domain | PNL |
| **Omega_h** | Parallel Mesh | 2D/3D | Triangular/Tetrahedral | Scalable HPC performance with MPI/OpenMP/CUDA | Open Source | Dan Ibanez |
| **OpenMesh** | Polygonal Mesh | 3D | Triangular | Generic data structure for polygonal meshes | Open Source | RWTH Aachen |
| **OpenVolumeMesh** | Polytopal Mesh | 3D | Various | Index-based data structure for polytopal meshes | Open Source | RWTH Aachen |
| **Overture** | Multiblock Grid | 2D/3D | Structured | Solution of PDEs on complicated domains | Public Domain | Center for Applied Scientific Computing |
| **PAMGEN** | Parallel Mesh | 2D/3D | Quadrilateral/Hexahedral | Hexahedral meshes of simple shapes in parallel | Public Domain | Sandia |
| **PARMGRIDGEN** | Coarse Grid | Various | Various | Algorithms for geometric multigrid methods | Public Domain | Irene Moulitsas |
| **QualMesh** | Volume Mesh | 3D | Tetrahedral | Quality volume mesh of polyhedral domains | Public Domain | Tamal K. Dey |
| **Qhull** | Convex Hull | General | Various | General dimension code for convex hulls, Delaunay | Public Domain | Brad Barber |
| **QMG** | MATLAB Mesh | 2D/3D | Triangular/Tetrahedral | Finite element mesh generation integrated into MATLAB | Public Domain | Stephen Vavasis |
| **QUIKGRID** | Scattered Data | 2D | Grid | Scattered data surface generator and viewer | Public Domain | John Coulthard |
| **SimLab** | Planar Triangulation | 2D | Triangular | Tool for guaranteed-quality triangulations | Public Domain | Paul Chew |
| **snappyHexMesh** | Hex-dominant | 3D | Hexahedral | Automatic hexahedral meshes from STL geometries | Open Source | OpenCFD |
| **SolidMesh** | Unstructured Grid | 2D/3D | Triangular/Tetrahedral | Unstructured grid generation system | Public Domain | MSU-ERC, MSU |
| **Stellar** | Mesh Improvement | 3D | Tetrahedral | Tetrahedral mesh improvement program | Public Domain | Bryan Klingner |
| **SurfRemesh** | Surface Remeshing | 3D | Triangular | Remeshing polygonal surfaces with Delaunay triangles | Public Domain | Tamal K. Dey |
| **SUS** | Mesh Optimization | 3D | Tetrahedral | Simultaneous untangling and smoothing | Public Domain | ULPGC IUSIANI |
| **T3D** | General Mesh | 3D | Triangular/Tetrahedral | Discretization of complex 3D domains | Public Domain | Daniel Rypl |
| **TCGRID** | Turbomachinery | 3D | Structured | Grid generation for turbomachinery blades | Public Domain | NASA Glenn Research Center |
| **Tetgen** | Tetrahedral | 3D | Tetrahedral | Exact Delaunay tetrahedralizations | Public Domain | Si Hang |
| **TMG** | Advancing Front | 2D | Triangular | Automatic triangular mesh generator | Public Domain | Maurizio Paolini |
| **Triangle** | Delaunay | 2D | Triangular | Exact constrained Delaunay triangulations | Public Domain | Jonathan Shewchuk |
| **UGRID** | Unstructured/Structured | 2D | Various | Rapid generation of smooth grids about airfoils | Public Domain | Donald Hawken |
| **Unamalla** | Rectangular Grid | 2D | Rectangular | Grid generation over irregular planar regions | Public Domain | Pablo Barrera-Sanchez |
| **Vcat2tets** | Medical Mesh | 3D | Tetrahedral | Multi-material tetrahedral meshes from 3D images | Public Domain | - |
| **VERDICT** | Mesh Quality | Various | Various | Library for computing quality metrics | Public Domain | Sandia National Laboratories |
| **VGRID** | Unstructured Grid | 3D | Triangular/Tetrahedral | Robust unstructured grid generation | Public Domain | Shahyar Pirzadeh |
| **VGM** | Structured Grid | 1D/2D/3D | Structured | Grid generation/manipulation tool | Public Domain | Stephen J. Alter |
| **ViennaGrid** | Generic Library | Various | Various | Library for structured and unstructured meshes | Open Source | Karl Rupp |
| **Volume** | Multi-block | 3D | Structured | Interactive multi-block structured volume grids | Public Domain | NASA Geometry Lab |
| **Voro++** | Voronoi Diagram | 3D | Voronoi | Computation of Voronoi diagram | Open Source | Chris Rycroft |
| **XGEN** | Moving Particle | 2D | Triangular | Moving particle scheme for triangle grid generation | Public Domain | Pavel Solin |
| **xprob** | Magnetic Field | 2D | Triangular | Automatic triangular mesh for magnetic field problems | Public Domain | UCD magnetics and machines group |
| **Yams** | Surface Mesh | 3D | Triangular | Geometric mesh and curvature-based mesh adaptation | Public Domain | Pascal Frey |
| **3DMAGGS** | Elliptic Grid | 3D | Structured | Elliptic volume grid generator for CFD | Public Domain | Stephen J. Alter |
| **ADINA UI** | Commercial FE | 3D | Tetrahedral | Surface and volume meshes from CAD data | Commercial | ADINA |
| **ANSYS CFX-Mesh** | Commercial CFD | 3D | Various | Automated surface/volume meshing | Commercial | Ansys |
| **ANSYS TurboGrid** | Commercial Turbomachinery | 3D | Structured | Lightning fast grid generation for turbomachinery | Commercial | Ansys |
| **Houdini** | Commercial Mechanical | 3D | Hexahedral | Unstructured hex meshing for mechanical engineering | Commercial | Algor |
| **Hypermesh** | Commercial CAE | 3D | Various | High performance FE pre-/post-processing | Commercial | Altair |
| **AMPSolid** | Commercial Semi-auto | 3D | Hexahedral | Semi-automatic mesh generator with ACIS integration | Commercial | AMPS Technologies |
| **SURFGEN/PEP** | Commercial CFD | 3D | Various | Surface and volume gridding for CFD simulations | Commercial | Analytical Methods Inc. |
| **ANSYS Tools** | Commercial Suite | 3D | Various | Model generation for ANSYS product line | Commercial | ANSYS Inc. |
| **MeshMaker** | Commercial Geosciences | 2D | Triangular/Quadrilateral | 2D element mesh generation for geosciences | Commercial | Argus Interware Inc. |
| **ANSA** | Commercial Automotive | 3D | Various | Automatic surface mesh generation and FEA preprocessing | Commercial | BETA CAE Systems |
| **BudMesh2D** | Commercial Rubber | 2D | Quadrilateral | All quadrilateral 2D mesh generator | Commercial | BUD |
| **SPIDER** | Commercial Octree | 3D | Tetrahedral | Octree-based meshing with boundary layers | Commercial | CAE Software Solutions |
| **AGPS** | Commercial Aerospace | 3D | Various | Aero-Grid Paneling System | Commercial | Calmar Research Corporation |
| **BOXERMesh** | Commercial CFD | 3D | Tetrahedral | Mesh generating system for CFD applications | Commercial | Cambridge Flow Solutions |
| **TIGER** | Commercial Turbomachinery | 3D | Structured | 3D structured grid for turbomachinery | Commercial | Catalpa Research Inc. |
| **Centaur** | Commercial Unstructured | 3D | Various | Complete unstructured grid generation package | Commercial | CentaurSoft |
| **TwinMesh** | Commercial PD Machines | 3D | Structured | Automatic structured meshes for positive displacement machines | Commercial | CFX Berlin |
| **GID** | Commercial General | 2D/3D | Various | 2D/3D structured/unstructured mesh generation | Commercial | Compass |
| **QUAD-GEN** | Commercial Quadrilateral | 2D | Quadrilateral | Automatic generator of quadrilateral meshes | Commercial | Computational Mechanics Australia |
| **ANISO-QUAD** | Commercial Anisotropic | 2D | Quadrilateral | Anisotropic quadrilateral mesher | Commercial | Computational Mechanics Australia |
| **CM2 MeshTools** | Commercial Delaunay | 2D/3D | Various | Delaunay meshers for various element types | Commercial | Computing Objects |
| **Trelis** | Commercial High-end | 3D | Various | High-end pre-processor based on Cubit | Commercial | csimsoft |
| **CastNet** | Commercial Hybrid | 3D | Hybrid | Automated hybrid mesher for CFD | Commercial | DHCAE Tools |
| **MEDINA** | Commercial CAE | 3D | Various | Universal CAE pre/post processing system | Commercial | T-Systems Digital Engineering |
| **HOMARD** | Commercial Adaptation | 2D/3D | Various | Mesh adaptation by refinement/unrefinement | Commercial | Electricité de France |
| **EleGrid** | Commercial Parametric | 3D | Various | Meshes on parametric surfaces | Commercial | Elements Research |
| **FEMAP** | Commercial FE | 3D | Various | Finite element preprocessor with 2D/3D meshing | Commercial | Siemens PLM |
| **CADfix** | Commercial Geometry | 3D | Various | Geometry repair and volume/surface meshing | Commercial | FEGS |
| **FEMGV** | Commercial General | 3D | Various | General-purpose pre-/post-processing | Commercial | Femsys Ltd |
| **MetaMesh** | Commercial Structured | 3D | Hexahedral | 3D structured conformal mesh | Commercial | Field Precision |
| **Mesh 4.5** | Commercial 2D | 2D | Triangular | 2D structured conformal mesh | Commercial | Field Precision |
| **GAMBIT** | Commercial CFD | 3D | Various | Single interface for geometry and meshing | Commercial | Fluent Inc. |
| **TGrid** | Commercial Hybrid | 3D | Hybrid | Advanced hybrid volume mesh generation | Commercial | Fluent Inc. |
| **CATIA Surface 2** | Commercial Surface | 3D | Triangular | Powerful surface mesher | Commercial | IBM |
| **ICEM CFD** | Commercial Suite | 3D | Various | Hexahedral, tetrahedral, and surface meshing | Commercial | Ansys Inc. |
| **MSC.AMS** | Commercial Manual | 3D | Various | Manual meshing and geometry creation | Commercial | MacNeal-Schwendler Corporation |
| **Mimics/3-matic** | Commercial Medical | 3D | Various | Medical image processing and mesh generation | Commercial | Materialise |
| **HexPress** | Commercial Hexahedral | 3D | Hexahedral | Unstructured hexahedral mesh generator | Commercial | NUMECA |
| **Pointwise** | Commercial Grid | 3D | Various | Surface and volume grid generation | Commercial | Pointwise Inc |
| **Grid Pro** | Commercial Automatic | 3D | Various | Automatic surface/volume grid generator | Commercial | Program Development Company |
| **NX** | Commercial FE | 3D | Various | Finite element preprocessing | Commercial | Siemens PLM |
| **MeshSim** | Commercial Automatic | 3D | Various | Automatic mesh generation from CAD models | Commercial | Simmetrix Inc. |
| **Kubrix** | Commercial Hexahedral | 3D | Hexahedral | All-hexahedral unstructured mesh generation | Commercial | Simulation Works, Inc. |
| **TetMesh-GHS3D** | Commercial Tetrahedral | 3D | Tetrahedral | Tetrahedral mesh generation | Commercial | Distene |
| **Yams** | Commercial Surface | 3D | Triangular | Surface mesh adaptation | Commercial | Distene |
| **MeshAdapt** | Commercial Adaptation | 3D | Various | Mesh adaptation | Commercial | Distene |
| **HEXOTIC** | Commercial Hexahedral | 3D | Hexahedral | Hexahedral mesh generation | Commercial | Distene |
| **SymLab** | Commercial Integrated | 3D | Various | Integrated structured/unstructured volume meshing | Commercial | Symscape |
| **Truegrid** | Commercial Multiblock | 3D | Structured | Multiblock structured grid generation | Commercial | XYZ Scientific Applications Inc. |

## Legend

### Element Types:
- **Triangular**: 2D triangles or 3D tetrahedra
- **Quadrilateral**: 2D quads or 3D hexahedra
- **Structured**: Regular grid patterns
- **Unstructured**: Irregular grid patterns
- **Hybrid**: Combination of element types
- **Surface**: Boundary/surface meshes only

### License Types:
- **Public Domain**: Free to use, no restrictions
- **Open Source**: Source code available, various licenses
- **Commercial**: Requires purchase/license
- **Dual License**: Multiple licensing options available

### Categories:
- **CFD**: Computational Fluid Dynamics focused
- **FEA**: Finite Element Analysis focused
- **Medical**: Biomedical applications
- **General**: Multi-purpose mesh generation
- **Specialized**: Domain-specific applications
