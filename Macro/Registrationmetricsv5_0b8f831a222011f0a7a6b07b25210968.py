"""


:author: Shumeng Jia
:contact: 
:email: shumeng.jia@mail.mcgill.ca
:organization: McGill University
:address: 
:copyright: 
:date: Apr 25 2025 19:31
:dragonflyVersion: 2024.1.0.1613
:UUID: 0b8f831a222011f0a7a6b07b25210968
"""

__version__ = '1.0.0'

# Action log Fri Apr 25 19:31:37 2025

# Macro name: Multi-res registration metrics

# Created by MacroEditor

# ********** BEGIN MACRO ********** #
"""
:name: Multi-res registration metrics
:execution: execute
"""

# blockly xml: %3Cxml%3E%3Cvariables%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%227cB%3B%5EOiYmlk%5ETg*gknBv%22%3ELRimage%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22%29%3AL4%5BouZL%5EV%3A@%5BE1IDP%25%22%3EHRimage%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22%7B0v%23%5E%29/5c%24T+5/%3FO%295%3Fw%22%3ELRdenoise%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22Xo+S%3B%2C925%7EN@%7CiF%60N%28NE%22%3ELRimage_sobel%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22j%3F5xnP%28+N%21t%3DKO1%7Dtmuj%22%3EHRimage_sobel%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22xkf82%7DE%5B%5B0MsSzR%28%7E*UJ%22%3EHRgauss%3C/variable%3E%3Cvariable%20type%3D%22int%22%20id%3D%22%24%3A%7DGG%7Bc9kXQ%7EPQRCMv%7B%23%22%3EHRxSpacing%3C/variable%3E%3Cvariable%20type%3D%22int%22%20id%3D%22%7ErsW%60IJ0%60-R%7Em%29hPvG%5DY%22%3EHRySpacing%3C/variable%3E%3Cvariable%20type%3D%22int%22%20id%3D%22%3FBxi6IK/Yd%23/-qbKCpv*%22%3EHRzSpacing%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22%60YrR2%3B@HUTQDGW6%5BSn%21x%22%3EHRgauss_sample%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22hy+%291o%608C%7Ch5Cw.Q*%5E1L%22%3EHRgauss_sample_sobel%3C/variable%3E%3Cvariable%20type%3D%22orsVisualShape%22%20id%3D%22%3BG%3AJ%7E2Gp%3ADxlk2%7DIh%2C1%60%22%3EBOX%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22SwUHWv%23i1xV%5DJ%60%7BlmH%21V%22%3ELRedge_extract%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22%3A%7D%5B%28Yts_gBFOS%60HTG.%3DY%22%3EHRedge_extract%3C/variable%3E%3Cvariable%20type%3D%22orsChannel%22%20id%3D%22b_QJE%5EYIJr_%3F1%5EA70T%7B%3B%22%3EaLRedge_extract%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22%25WOvs%7D%23nFK6q9a5DhLy%25%22%3ELRminFloat%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22d0T3yA.a%28H%3Dx%3Bktv9_+b%22%3ELRmaxFloat%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%22g-%3D%7CHDvW%7CD_%29w%5Dwng-%3Fm%22%3ELRfullROI%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%22u@%5Byxp8M%2CMgD%7B%3BOlEb%23O%22%3ELRedgeROI%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22pj%254K%28%3DA%60H%3Bb1avx%60@%29s%22%3EHRminFloat%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22X7a/J%5DKj%5EACzsO*%5EewDS%22%3EHRmaxFloat%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%22*jz5%7D%7B_90x4G%3Bg%7DKkE%7B%60%22%3EHRfullROI%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%22Xvr%7EX%2C%7E%21Kuh8Z04K1MFq%22%3EHRedgeROI%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22xky7%7DRHbJG%25-%3D_Z%5DMU5c%22%3EaLRminFloat%3C/variable%3E%3Cvariable%20type%3D%22float%22%20id%3D%22%60HY7QsT0sb_5nKLC%3Fs%29Y%22%3EaLRmaxFloat%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%225Zu%7BS@HKG%3BshD%7B%28wY%28s*%22%3EaLRfullROI%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%22%7Es%29P0S@%24%24q%3Aig%3FKWZuvY%22%3EaLRedgeROI%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%22%3Am%5B%7DN%5BXdsvViI%21ui0%21%28t%22%3EHR_LR%3C/variable%3E%3Cvariable%20type%3D%22orsROI%22%20id%3D%22/D72K*e%7B.N@r*qFiqIha%22%3EHR_aLR%3C/variable%3E%3Cvariable%20type%3D%22str%22%20id%3D%22%7BfX%60Fz5HL-ZWL-yKc%5EB%2C%22%3Eresult%3C/variable%3E%3C/variables%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%222N2%24%5E%3A%29hmwL@%5D%3D@i7rS%5E%22%20x%3D%22-228%22%20y%3D%22-2169%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%227cB%3B%5EOiYmlk%5ETg*gknBv%22%20variabletype%3D%22orsChannel%22%3ELRimage%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22object_chooser%22%20id%3D%22GQ%25%5Egs3VMJ%7C%5EL%5E_-%3Dwzc%22%3E%3Cmutation%20type%3D%22orsChannel%22%20default%3D%22LRimage%22%3E%3C/mutation%3E%3Cfield%20name%3D%22TYPE%22%3EorsChannel%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3ELRimage%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%7D-_%5ExdY6%7Eryg6_WK%3B_@U%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29%3AL4%5BouZL%5EV%3A@%5BE1IDP%25%22%20variabletype%3D%22orsChannel%22%3EHRimage%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22object_chooser%22%20id%3D%22%3B1%7E2b.VmF61yd%3BF4nO%7Du%22%3E%3Cmutation%20type%3D%22orsChannel%22%20default%3D%22HRimage%22%3E%3C/mutation%3E%3Cfield%20name%3D%22TYPE%22%3EorsChannel%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3EHRimage%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_image_filter%22%20id%3D%22CEMA7VsO%21@0*iGHefFOW%22%20inline%3D%22false%22%3E%3Cmutation%20uuid%3D%22f05bebb0ea3211e683dec86000a21918%22%3E%3C/mutation%3E%3Cfield%20name%3D%22kernelDim%22%3E3D%3C/field%3E%3Cvalue%20name%3D%22UUID%22%3E%3Cblock%20type%3D%22ors_image_filter_uuid%22%20id%3D%22_H%21QXx.wg.tO%608b%233u3J%22%3E%3Cfield%20name%3D%22NAME%22%3Ef05bebb0ea3211e683dec86000a21918%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22sigma%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22p%3D6-%60v%7Eu1%3FU@%29lSf/PSm%22%3E%3Cfield%20name%3D%22NUM%22%3E0.9999999999999999%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22kernelSize%22%3E%3Cblock%20type%3D%22kernel_size%22%20id%3D%22p5%60%3A%7E%24%7Eq%25g%28Pg@%7C%7BVH%24Q%22%3E%3Cfield%20name%3D%22SIZE%22%3Eindex3%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22input1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22/A%5Dv%7EDxQB%60ED%7DllPg%5D%25f%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%227cB%3B%5EOiYmlk%5ETg*gknBv%22%20variabletype%3D%22orsChannel%22%3ELRimage%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22output1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22T%3B%7CZ+@GV%7ECx%3FV%21wu6%2Ci0%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7B0v%23%5E%29/5c%24T+5/%3FO%295%3Fw%22%20variabletype%3D%22orsChannel%22%3ELRdenoise%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_image_filter%22%20id%3D%22XAvE%7C_LfC3J5t3@%7B6R-F%22%20inline%3D%22false%22%3E%3Cmutation%20uuid%3D%22369fae80ea3c11e6a9f1c86000a21918%22%3E%3C/mutation%3E%3Cfield%20name%3D%22gaussian%22%3ETRUE%3C/field%3E%3Cfield%20name%3D%22kernelDim%22%3E3D%3C/field%3E%3Cvalue%20name%3D%22UUID%22%3E%3Cblock%20type%3D%22ors_image_filter_uuid%22%20id%3D%22huI%28_Hi9%5D1%60%5B-%28+%3ABLF5%22%3E%3Cfield%20name%3D%22NAME%22%3E369fae80ea3c11e6a9f1c86000a21918%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22input1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%224p+Q7/V%3Bv9+yu_7z9%23m1%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7B0v%23%5E%29/5c%24T+5/%3FO%295%3Fw%22%20variabletype%3D%22orsChannel%22%3ELRdenoise%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22output1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22e0%2CH8c/7kPses3J%3ALg%3D%24%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Xo+S%3B%2C925%7EN@%7CiF%60N%28NE%22%20variabletype%3D%22orsChannel%22%3ELRimage_sobel%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_image_filter%22%20id%3D%22%3FT%5E%6080oKP%3D%21%21PC2slMxH%22%20inline%3D%22false%22%3E%3Cmutation%20uuid%3D%22369fae80ea3c11e6a9f1c86000a21918%22%3E%3C/mutation%3E%3Cfield%20name%3D%22gaussian%22%3ETRUE%3C/field%3E%3Cfield%20name%3D%22kernelDim%22%3E3D%3C/field%3E%3Cvalue%20name%3D%22UUID%22%3E%3Cblock%20type%3D%22ors_image_filter_uuid%22%20id%3D%22%3BL+_7QJHL%7EUDo_gKI%5DxC%22%3E%3Cfield%20name%3D%22NAME%22%3E369fae80ea3c11e6a9f1c86000a21918%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22input1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22iSU-u2J*aJFbNi5.X%3DEH%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29%3AL4%5BouZL%5EV%3A@%5BE1IDP%25%22%20variabletype%3D%22orsChannel%22%3EHRimage%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22output1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%5Bqwj%7BC%3Dwc//%21YauyG%23n%3A%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22j%3F5xnP%28+N%21t%3DKO1%7Dtmuj%22%20variabletype%3D%22orsChannel%22%3EHRimage_sobel%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_image_filter%22%20id%3D%22n%25tP%5DNFBubBWOQ%3BJeF%7C*%22%20inline%3D%22false%22%3E%3Cmutation%20uuid%3D%22f05bebb0ea3211e683dec86000a21918%22%3E%3C/mutation%3E%3Cfield%20name%3D%22kernelDim%22%3E3D%3C/field%3E%3Cvalue%20name%3D%22UUID%22%3E%3Cblock%20type%3D%22ors_image_filter_uuid%22%20id%3D%22MR%24q%7EOx64*0o8ePglEa%7B%22%3E%3Cfield%20name%3D%22NAME%22%3Ef05bebb0ea3211e683dec86000a21918%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22sigma%22%3E%3Cblock%20type%3D%22value_chooser%22%20id%3D%22%5DuOcM%21Eh1H5tO0g%3B2rN%21%22%3E%3Cfield%20name%3D%22TYPE%22%3EFloat%3A%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3EStandard%20deviation%3C/field%3E%3Cfield%20name%3D%22DEFAULT%22%3E%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22kernelSize%22%3E%3Cblock%20type%3D%22value_chooser%22%20id%3D%223%7D0Rz12ON%7D0h%3A+jYZ%3FTJ%22%3E%3Cfield%20name%3D%22TYPE%22%3EInteger%3A%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3EKernel%20Size%3C/field%3E%3Cfield%20name%3D%22DEFAULT%22%3E%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22input1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22tV-Q%7C4%23O%7EvjyG%219jtuS%3F%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29%3AL4%5BouZL%5EV%3A@%5BE1IDP%25%22%20variabletype%3D%22orsChannel%22%3EHRimage%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22output1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%2249%5D%2C/rjSbH*DK%3Dg4*jwn%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xkf82%7DE%5B%5B0MsSzR%28%7E*UJ%22%20variabletype%3D%22orsChannel%22%3EHRgauss%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22lz4fpwW8nFO%7E%5ELMA%5B6Re%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%24%3A%7DGG%7Bc9kXQ%7EPQRCMv%7B%23%22%20variabletype%3D%22int%22%3EHRxSpacing%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%228%3AH6Y1pyWoo_K%5E8R_UKi%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getXSpacing%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%229u7/u%5B+H%7Ddy0V%7B%3DinBE5%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xkf82%7DE%5B%5B0MsSzR%28%7E*UJ%22%20variabletype%3D%22orsChannel%22%3EHRgauss%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22%23%7DmH%7DZWnKW98v%7Cu%7CGg7B%22%3E%3Cfield%20name%3D%22method%22%3EgetXSpacing%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22cJ.7s%7E%29l%60daRzj2eF/bF%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7ErsW%60IJ0%60-R%7Em%29hPvG%5DY%22%20variabletype%3D%22int%22%3EHRySpacing%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22%3B%60%5Bbuqc%7EYR%3DE-Z5%5Bh3.m%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getYSpacing%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22N8oXKvLyNhN./P%60%7C98MN%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xkf82%7DE%5B%5B0MsSzR%28%7E*UJ%22%20variabletype%3D%22orsChannel%22%3EHRgauss%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22yrcY%3B@3RyXEA%23GfuuGw2%22%3E%3Cfield%20name%3D%22method%22%3EgetYSpacing%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22H2nt@K@x1HqMRYNvDu%7DS%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3FBxi6IK/Yd%23/-qbKCpv*%22%20variabletype%3D%22int%22%3EHRzSpacing%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22p%7B%3FH%29JW70g%5D0@%28%2C%3DD%7Dm%5D%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getZSpacing%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%60f%3AEaR9_b%3DTwX%7E@Fx/FN%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xkf82%7DE%5B%5B0MsSzR%28%7E*UJ%22%20variabletype%3D%22orsChannel%22%3EHRgauss%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22%5D%21n%21%7BnPB%23k%60oN%7C4cDd8N%22%3E%3Cfield%20name%3D%22method%22%3EgetZSpacing%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_interface_method%22%20id%3D%22NAcyyKo-o3%28xt2PwH7bq%22%20inline%3D%22false%22%3E%3Cmutation%20module%3D%22OrsPythonPlugins.OrsDatasetSampler.OrsDatasetSampler%22%20method%3D%22OrsDatasetSampler.sampleDatasetInSpacing%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22module%22%3E%3Cblock%20type%3D%22ors_interface_module_selector%22%20id%3D%22XTM%7CI%7B7%5B5%7BbvS%21-U5tAQ%22%3E%3Cfield%20name%3D%22module%22%3EOrsPythonPlugins.OrsDatasetSampler.OrsDatasetSampler%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22ors_interface_method_selector%22%20id%3D%221RZYSnC1%60o%24%7C%3Fat/st%29f%22%3E%3Cfield%20name%3D%22method%22%3EOrsDatasetSampler.sampleDatasetInSpacing%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22dataset%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22kqc%60mQHnIRYMaih%5D4wD.%22%3E%3C/shadow%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22_HdWk3%7BJ+%7DayAz9Gv%24r%29%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xkf82%7DE%5B%5B0MsSzR%28%7E*UJ%22%20variabletype%3D%22orsChannel%22%3EHRgauss%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22xSpacing%22%3E%3Cblock%20type%3D%22math_arithmetic%22%20id%3D%22tRrmqwE6700Nm_XAtO@G%22%3E%3Cfield%20name%3D%22OP%22%3EMULTIPLY%3C/field%3E%3Cvalue%20name%3D%22A%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22c%3BOnZIpN%5E5%7CE%7E+*9NibX%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%24%3A%7DGG%7Bc9kXQ%7EPQRCMv%7B%23%22%20variabletype%3D%22int%22%3EHRxSpacing%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22B%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22%3D%5D@ZT%5Dpy@q%7D%7DtH%3D3%25JS%29%22%3E%3Cfield%20name%3D%22NUM%22%3E2%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22ySpacing%22%3E%3Cblock%20type%3D%22math_arithmetic%22%20id%3D%225Dm934-@NegzF%3D*%21@%7E5m%22%3E%3Cfield%20name%3D%22OP%22%3EMULTIPLY%3C/field%3E%3Cvalue%20name%3D%22A%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%227.%5En.%5Bw%7EZvTTzl-VQO6b%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7ErsW%60IJ0%60-R%7Em%29hPvG%5DY%22%20variabletype%3D%22int%22%3EHRySpacing%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22B%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22MLP7YYO.-Z8%7BYvi2M%60qa%22%3E%3Cfield%20name%3D%22NUM%22%3E2%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22zSpacing%22%3E%3Cblock%20type%3D%22math_arithmetic%22%20id%3D%22uE%5D%3A1hT%5E6%24Ka9eTlrI6r%22%3E%3Cfield%20name%3D%22OP%22%3EMULTIPLY%3C/field%3E%3Cvalue%20name%3D%22A%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22b.uVq%2C%3D%7COGX%7Ejyn%25suwe%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3FBxi6IK/Yd%23/-qbKCpv*%22%20variabletype%3D%22int%22%3EHRzSpacing%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22B%22%3E%3Cblock%20type%3D%22math_number%22%20id%3D%22%7C+W_%5B-puq%25em0N_%60NW%3D2%22%3E%3Cfield%20name%3D%22NUM%22%3E2%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22samplingType%22%3E%3Cblock%20type%3D%22python_code%22%20id%3D%22yq%3FK%5D@%7Eo%5EDT@A%5EKBw6T+%22%3E%3Cfield%20name%3D%22CODE%22%3ECOMWrapper.ORS_def.CxvSamplingMethod.CxvSamplingNearest%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22createNewDataset%22%3E%3Cblock%20type%3D%22logic_boolean%22%20id%3D%225fHFaWuP1WL_/.H%24ivl%2C%22%3E%3Cfield%20name%3D%22BOOL%22%3ETRUE%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22newDataset%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22yPmK%5D%3A%3D7X%60@bGTazgJ%5BR%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%60YrR2%3B@HUTQDGW6%5BSn%21x%22%20variabletype%3D%22orsChannel%22%3EHRgauss_sample%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22%3D/%3AE-mFqv87EEE%7B%21*Jc%5B%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%60YrR2%3B@HUTQDGW6%5BSn%21x%22%20variabletype%3D%22orsChannel%22%3EHRgauss_sample%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_set_title%22%20id%3D%22plu%285Ad%5B7%7E%2C8%21Hk%21Cpg/%22%3E%3Cfield%20name%3D%22ORS%22%20id%3D%22%60YrR2%3B@HUTQDGW6%5BSn%21x%22%20variabletype%3D%22orsChannel%22%3EHRgauss_sample%3C/field%3E%3Cvalue%20name%3D%22TITLE%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22eiBvP3b%28h%29_AU%3Fj%5E/Sp_%22%3E%3Cfield%20name%3D%22TEXT%22%3EaLR%20image%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_image_filter%22%20id%3D%22a%251sdb5@IMv55%7DzE%3Fp%7D%5E%22%20inline%3D%22false%22%3E%3Cmutation%20uuid%3D%22369fae80ea3c11e6a9f1c86000a21918%22%3E%3C/mutation%3E%3Cfield%20name%3D%22gaussian%22%3EFALSE%3C/field%3E%3Cfield%20name%3D%22kernelDim%22%3E3D%3C/field%3E%3Cvalue%20name%3D%22UUID%22%3E%3Cblock%20type%3D%22ors_image_filter_uuid%22%20id%3D%22%7CC%25%7Eo%2C3%24%29%28%29e%5BL2%7DW/2*%22%3E%3Cfield%20name%3D%22NAME%22%3E369fae80ea3c11e6a9f1c86000a21918%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22input1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22.M%2Cv%3Fe01O%24b0%3F%3AWo%3FE%7Ci%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%60YrR2%3B@HUTQDGW6%5BSn%21x%22%20variabletype%3D%22orsChannel%22%3EHRgauss_sample%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22output1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22BmDr%60bC*%25%5EWywQCFSi%60r%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22hy+%291o%608C%7Ch5Cw.Q*%5E1L%22%20variabletype%3D%22orsChannel%22%3EHRgauss_sample_sobel%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%21oxT%5Dj%7BolsiX%60hS%3AuMR_%22%3E%3Cmutation%20output_type_at_creation%3D%22orsVisualShape%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3BG%3AJ%7E2Gp%3ADxlk2%7DIh%2C1%60%22%20variabletype%3D%22orsVisualShape%22%3EBOX%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsVisualShape%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22object_chooser%22%20id%3D%22ojP95Ii%287st%5D%3BKgyQqP4%22%3E%3Cmutation%20type%3D%22orsVisualShape%22%20default%3D%22Metrics%20box%22%3E%3C/mutation%3E%3Cfield%20name%3D%22TYPE%22%3EorsVisualShape%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3EMetrics%20box%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22@A%3A@YSq%3DyR%3Aj/m%7E3z@kq%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22SwUHWv%23i1xV%5DJ%60%7BlmH%21V%22%20variabletype%3D%22orsChannel%22%3ELRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22python_code%22%20id%3D%22gkDzXxh%3B%23u.UB4oiw%5B%2C%7C%22%3E%3Cfield%20name%3D%22CODE%22%3EextractBoxFromChannel_bdfbc9a8110b11e8819130e37aed33ab.createDatasetFromVisualBox%28sourceDataset%3DLRimage_sobel%2C%20visualBox%3DBOX%2C%20timestep%3D0%2C%20title%3D%27LR%20edge%20extract%27%29%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22bg%7BKMG%25%7DlZH4U2*oY%28p1%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3A%7D%5B%28Yts_gBFOS%60HTG.%3DY%22%20variabletype%3D%22orsChannel%22%3EHRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22python_code%22%20id%3D%22dsl%3F%7Ceu%3A%23_O%3AWwEO%25-MM%22%3E%3Cfield%20name%3D%22CODE%22%3EextractBoxFromChannel_bdfbc9a8110b11e8819130e37aed33ab.createDatasetFromVisualBox%28sourceDataset%3DHRimage_sobel%2C%20visualBox%3DBOX%2C%20timestep%3D0%2C%20title%3D%27HR%20edge%20extract%27%29%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22M%3A%3BSwMf0gg%3B%7CV%5Bzg%5E%3Dl%24%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22b_QJE%5EYIJr_%3F1%5EA70T%7B%3B%22%20variabletype%3D%22orsChannel%22%3EaLRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22python_code%22%20id%3D%22mE%3FaGMH%7CF0%3FU1jvIaeTH%22%3E%3Cfield%20name%3D%22CODE%22%3EextractBoxFromChannel_bdfbc9a8110b11e8819130e37aed33ab.createDatasetFromVisualBox%28sourceDataset%3DHRgauss_sample_sobel%2C%20visualBox%3DBOX%2C%20timestep%3D0%2C%20title%3D%27aLR%20edge%20extract%27%29%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22S@tCC%21+DZfgv%28*znT@ms%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%25WOvs%7D%23nFK6q9a5DhLy%25%22%20variabletype%3D%22float%22%3ELRminFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22hLTZCi.%3Fua%29L%23+Dq%28%245%5D%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getMinimumValue%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22idc6xq+n%2Cp7%5D%5D%23kHqP/B%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22SwUHWv%23i1xV%5DJ%60%7BlmH%21V%22%20variabletype%3D%22orsChannel%22%3ELRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22MG9ipJPr0n%28.1%3Av%7Dd%3B2-%22%3E%3Cfield%20name%3D%22method%22%3EgetMinimumValue%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%3Bo%25qo%2CCB7Bfg.Bz%3DHE1o%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22d0T3yA.a%28H%3Dx%3Bktv9_+b%22%20variabletype%3D%22float%22%3ELRmaxFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22xCOW%7B2%7DRX6%2CfH0Gg%7DqIT%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getMaximumValue%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22HN%23@/zGlkV*%5E-.SH%5B4P2%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22SwUHWv%23i1xV%5DJ%60%7BlmH%21V%22%20variabletype%3D%22orsChannel%22%3ELRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22_/KMf%7DLf%3BW%29D/J%24meNv-%22%3E%3Cfield%20name%3D%22method%22%3EgetMaximumValue%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22nM%5Bl%23K%5EK%5EFC%60TO%29g%28D1_%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22g-%3D%7CHDvW%7CD_%29w%5Dwng-%3Fm%22%20variabletype%3D%22orsROI%22%3ELRfullROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22create_roi_range%22%20id%3D%22Yhu-k9V%248%2C5Z%253*4%28M%7C%5E%22%3E%3Cvalue%20name%3D%22CHANNEL%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22Yv/dj/E8PQ-JU%7Ee-Rad2%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22SwUHWv%23i1xV%5DJ%60%7BlmH%21V%22%20variabletype%3D%22orsChannel%22%3ELRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22MIN%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22O1ivHRpfRI*m5ap%7D.ut%7B%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%25WOvs%7D%23nFK6q9a5DhLy%25%22%20variabletype%3D%22float%22%3ELRminFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22MAX%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%3B7u.%23%60%2Cf%3Dd%23mOva%25%7EZP.%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22d0T3yA.a%28H%3Dx%3Bktv9_+b%22%20variabletype%3D%22float%22%3ELRmaxFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22c%7DY@zX9VY5pN%3BSC12hjE%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22u@%5Byxp8M%2CMgD%7B%3BOlEb%23O%22%20variabletype%3D%22orsROI%22%3ELRedgeROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22roi_otsu_foreground%22%20id%3D%22yFo%5DR%60%3BDKlMK-gCBUK%3Am%22%3E%3Cvalue%20name%3D%22ROI%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22a%24n%7D*%5E%5E3k9dA%7Bv6GYT@r%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22g-%3D%7CHDvW%7CD_%29w%5Dwng-%3Fm%22%20variabletype%3D%22orsROI%22%3ELRfullROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22CHANNEL%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22Y%2CAPv.4SCkO8RKtEmY3%60%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22SwUHWv%23i1xV%5DJ%60%7BlmH%21V%22%20variabletype%3D%22orsChannel%22%3ELRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_set_title%22%20id%3D%22%3FGgPss0%5E6r%28Flxn%253AkW%22%3E%3Cfield%20name%3D%22ORS%22%20id%3D%22u@%5Byxp8M%2CMgD%7B%3BOlEb%23O%22%20variabletype%3D%22orsROI%22%3ELRedgeROI%3C/field%3E%3Cvalue%20name%3D%22TITLE%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22OZSudu6U*%21-sIQ%7ELY%5EHH%22%3E%3Cfield%20name%3D%22TEXT%22%3ELR%20edge%20ROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22sm4D%7Bpxw%60w3@%5EY%7Eax@2e%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22pj%254K%28%3DA%60H%3Bb1avx%60@%29s%22%20variabletype%3D%22float%22%3EHRminFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22%7BY%7B%7BwRe%3F-%5Ebi@o%7CT0P%21U%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getMinimumValue%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22/i846aGOI%7D8eTDbji2k%3D%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3A%7D%5B%28Yts_gBFOS%60HTG.%3DY%22%20variabletype%3D%22orsChannel%22%3EHRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22_%7BRASzC%25%21@_3Ns%2959%7Ce1%22%3E%3Cfield%20name%3D%22method%22%3EgetMinimumValue%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%7Bv1%3F12f2mS%24nGZ%5Da%5E-BP%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22X7a/J%5DKj%5EACzsO*%5EewDS%22%20variabletype%3D%22float%22%3EHRmaxFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22%3Dwat%5BZLiqm4JuV4+K%21m%7E%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getMaximumValue%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22cEDmCVkp.FBPNyIgWVd%21%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3A%7D%5B%28Yts_gBFOS%60HTG.%3DY%22%20variabletype%3D%22orsChannel%22%3EHRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%225paj%7C8%2C%60%3D/yxdK%7BAr.QF%22%3E%3Cfield%20name%3D%22method%22%3EgetMaximumValue%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%227HV%25Lyl%23AAtkswF%25Y3az%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22*jz5%7D%7B_90x4G%3Bg%7DKkE%7B%60%22%20variabletype%3D%22orsROI%22%3EHRfullROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22create_roi_range%22%20id%3D%22%3AA/%29*JR/%21%3AGqYU%2CZlZA*%22%3E%3Cvalue%20name%3D%22CHANNEL%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22M3m/%3Daj2%60lX%7BVZyNEUww%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3A%7D%5B%28Yts_gBFOS%60HTG.%3DY%22%20variabletype%3D%22orsChannel%22%3EHRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22MIN%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%3D%3AD%7C%2Cf%7B%5Bp%3AhYM%3A%3Fm3_H%60%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22pj%254K%28%3DA%60H%3Bb1avx%60@%29s%22%20variabletype%3D%22float%22%3EHRminFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22MAX%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22*%7CH9q%7C6/%24sd0%28cAr9QRJ%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22X7a/J%5DKj%5EACzsO*%5EewDS%22%20variabletype%3D%22float%22%3EHRmaxFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%60UuwIzXLK3h%24y1xQXH2E%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Xvr%7EX%2C%7E%21Kuh8Z04K1MFq%22%20variabletype%3D%22orsROI%22%3EHRedgeROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22roi_otsu_foreground%22%20id%3D%22%23fle%7CKsjjs%5DgpV4%23%7Dg%219%22%3E%3Cvalue%20name%3D%22ROI%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%229aaPD%28gtYRi%28%5E./s@OrJ%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22*jz5%7D%7B_90x4G%3Bg%7DKkE%7B%60%22%20variabletype%3D%22orsROI%22%3EHRfullROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22CHANNEL%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22x%7DG/g_j%25v%23.-A45%5D*.%3F%23%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3A%7D%5B%28Yts_gBFOS%60HTG.%3DY%22%20variabletype%3D%22orsChannel%22%3EHRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_set_title%22%20id%3D%22%29b9BXX%5E%2C%3F%7C3%25%3BWh1f%7D3F%22%3E%3Cfield%20name%3D%22ORS%22%20id%3D%22Xvr%7EX%2C%7E%21Kuh8Z04K1MFq%22%20variabletype%3D%22orsROI%22%3EHRedgeROI%3C/field%3E%3Cvalue%20name%3D%22TITLE%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22uj%23QezU%3F%5Eq9P%7DLF2sH+@%22%3E%3Cfield%20name%3D%22TEXT%22%3EHR%20edge%20ROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22kYLCj%3Fd5%2C.WRNh/%3AKIcX%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xky7%7DRHbJG%25-%3D_Z%5DMU5c%22%20variabletype%3D%22float%22%3EaLRminFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22%24A%60%7EE@p.Fz%7D%7EeN@%21LjgW%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getMinimumValue%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22K%29H%7D%2C%25%23Vb%5Dl%29.%7CP1tNRO%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22b_QJE%5EYIJr_%3F1%5EA70T%7B%3B%22%20variabletype%3D%22orsChannel%22%3EaLRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22RkU%5BxkdH.n%3FHr%7D%3F%3B*c%23*%22%3E%3Cfield%20name%3D%22method%22%3EgetMinimumValue%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%7CQ2l24%3Dr%7B%2CPK%5E%3Ba5%7EqU%3B%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%60HY7QsT0sb_5nKLC%3Fs%29Y%22%20variabletype%3D%22float%22%3EaLRmaxFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22kGsmkf%2Cho2bkmSF%3DPoUB%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsChannel%22%20method%3D%22getMaximumValue%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22RapeR%3Bw/@cD9%23KKBJet%7B%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22b_QJE%5EYIJr_%3F1%5EA70T%7B%3B%22%20variabletype%3D%22orsChannel%22%3EaLRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22iX%21N_x+j%5D78ngqKLTZu/%22%3E%3Cfield%20name%3D%22method%22%3EgetMaximumValue%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%7B%3B%7C3%2CuqcS%252bmAYd%7Ced4%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%225Zu%7BS@HKG%3BshD%7B%28wY%28s*%22%20variabletype%3D%22orsROI%22%3EaLRfullROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22create_roi_range%22%20id%3D%22uD%7CKxuKX6v6sICW@F1%5B%21%22%3E%3Cvalue%20name%3D%22CHANNEL%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22smDo%3FAfnQ-s/jZ%7B@YV%2Cj%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22b_QJE%5EYIJr_%3F1%5EA70T%7B%3B%22%20variabletype%3D%22orsChannel%22%3EaLRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22MIN%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%23iQw///@op_n%28.uY%3D%7DSo%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xky7%7DRHbJG%25-%3D_Z%5DMU5c%22%20variabletype%3D%22float%22%3EaLRminFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22MAX%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22O%7EGgul%29%3BNOgYH%23*Xq%23cJ%22%3E%3Cmutation%20output_type_at_creation%3D%22float%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%60HY7QsT0sb_5nKLC%3Fs%29Y%22%20variabletype%3D%22float%22%3EaLRmaxFloat%3C/field%3E%3Cfield%20name%3D%22type%22%3Efloat%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22_wIPMY%25%7DeDLC%7BH%3A%7Db%60fu%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7Es%29P0S@%24%24q%3Aig%3FKWZuvY%22%20variabletype%3D%22orsROI%22%3EaLRedgeROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22roi_otsu_foreground%22%20id%3D%22f%3Bv6e_cqGvnLZ%2ChV6rGl%22%3E%3Cvalue%20name%3D%22ROI%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%221QIU+sY%7CtMyTRXfIr1c%25%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%225Zu%7BS@HKG%3BshD%7B%28wY%28s*%22%20variabletype%3D%22orsROI%22%3EaLRfullROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22CHANNEL%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22LS4zO%7D25%3Dbk%2C9fpAz.%29/%22%3E%3Cmutation%20output_type_at_creation%3D%22orsChannel%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22b_QJE%5EYIJr_%3F1%5EA70T%7B%3B%22%20variabletype%3D%22orsChannel%22%3EaLRedge_extract%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsChannel%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_set_title%22%20id%3D%22%25vEBE%23%3Azv@kK6IEa%7E_z%5D%22%3E%3Cfield%20name%3D%22ORS%22%20id%3D%22%7Es%29P0S@%24%24q%3Aig%3FKWZuvY%22%20variabletype%3D%22orsROI%22%3EaLRedgeROI%3C/field%3E%3Cvalue%20name%3D%22TITLE%22%3E%3Cblock%20type%3D%22text%22%20id%3D%227X%23BKtRj1skG14%7ESv/Vk%22%3E%3Cfield%20name%3D%22TEXT%22%3EaLR%20edge%20ROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%228a8S%3A%5E%3D%3A%60y%23c@3%2Cm%29Ie3%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22SwUHWv%23i1xV%5DJ%60%7BlmH%21V%22%20variabletype%3D%22orsChannel%22%3ELRedge_extract%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22%7DfFBrA%24eNea%292q%25M-PHP%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3A%7D%5B%28Yts_gBFOS%60HTG.%3DY%22%20variabletype%3D%22orsChannel%22%3EHRedge_extract%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%228%60%25.rs5%7CHcJS5HRER%23dh%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22b_QJE%5EYIJr_%3F1%5EA70T%7B%3B%22%20variabletype%3D%22orsChannel%22%3EaLRedge_extract%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22BihZA%3Dq@L%3FIz9j1b*jEA%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22u@%5Byxp8M%2CMgD%7B%3BOlEb%23O%22%20variabletype%3D%22orsROI%22%3ELRedgeROI%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22%5Em4c4V%7Dk%3FJmydQ%24QZ@%29.%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Xvr%7EX%2C%7E%21Kuh8Z04K1MFq%22%20variabletype%3D%22orsROI%22%3EHRedgeROI%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22yw%7BbBVyir%21/%24+k%24gUf-N%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7Es%29P0S@%24%24q%3Aig%3FKWZuvY%22%20variabletype%3D%22orsROI%22%3EaLRedgeROI%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22kk0tK%7Ekh-6%3F2ra%28u%3Fyj%2C%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22j%3F5xnP%28+N%21t%3DKO1%7Dtmuj%22%20variabletype%3D%22orsChannel%22%3EHRimage_sobel%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22%243Po%21Cc*%5Dd2-QL%29AFM%3D@%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7B0v%23%5E%29/5c%24T+5/%3FO%295%3Fw%22%20variabletype%3D%22orsChannel%22%3ELRdenoise%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22v%23+.+k%24tjoe%7B9HGA7%60p.%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Xo+S%3B%2C925%7EN@%7CiF%60N%28NE%22%20variabletype%3D%22orsChannel%22%3ELRimage_sobel%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22%28@DqEJyz%5Ds_MpK%3AzypJ%3F%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22xkf82%7DE%5B%5B0MsSzR%28%7E*UJ%22%20variabletype%3D%22orsChannel%22%3EHRgauss%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22g%5Evk+%24Frch31V*FHtY%5D%29%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22hy+%291o%608C%7Ch5Cw.Q*%5E1L%22%20variabletype%3D%22orsChannel%22%3EHRgauss_sample_sobel%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22Pe%7B1.R%29rU49do%2Cpuzc@n%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22*jz5%7D%7B_90x4G%3Bg%7DKkE%7B%60%22%20variabletype%3D%22orsROI%22%3EHRfullROI%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22nC%7CzO%5B%7D5%21/%3Ae%5BHtCH%25ZI%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22g-%3D%7CHDvW%7CD_%29w%5Dwng-%3Fm%22%20variabletype%3D%22orsROI%22%3ELRfullROI%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_delete_object%22%20id%3D%22Sq8ea%7B%5EJSL%25uA3%25cdRs6%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%225Zu%7BS@HKG%3BshD%7B%28wY%28s*%22%20variabletype%3D%22orsROI%22%3EaLRfullROI%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22CU-ry%3B%60%60%3AOU%29O.-l%5DQ--%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3Am%5B%7DN%5BXdsvViI%21ui0%21%28t%22%20variabletype%3D%22orsROI%22%3EHR_LR%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22roi_boolean_operations%22%20id%3D%22j9GKq1-%5DFY+F%3D%5DQDIK/F%22%3E%3Cfield%20name%3D%22OPERATION%22%3EAMINUSB%3C/field%3E%3Cfield%20name%3D%22EMPTY%22%3EFALSE%3C/field%3E%3Cvalue%20name%3D%22ROI1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22aLhV3l7I%25%25O%25q.x*%5BO%25H%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22u@%5Byxp8M%2CMgD%7B%3BOlEb%23O%22%20variabletype%3D%22orsROI%22%3ELRedgeROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22ROI2%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%2218%3BMWSdM%29A%5E7Jchr%5BoQ%3D%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Xvr%7EX%2C%7E%21Kuh8Z04K1MFq%22%20variabletype%3D%22orsROI%22%3EHRedgeROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22wzHxWXkP%5EayTNarH9%28%5B0%22%3E%3Cfield%20name%3D%22TEXT%22%3ELRedge-HRedge%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22%28B%5E5q*.fUmw%25W@dA%7DSQa%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22/D72K*e%7B.N@r*qFiqIha%22%20variabletype%3D%22orsROI%22%3EHR_aLR%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22roi_boolean_operations%22%20id%3D%22n2xD8Zz5jQM38Zj%3D%25a%3Bu%22%3E%3Cfield%20name%3D%22OPERATION%22%3EAMINUSB%3C/field%3E%3Cfield%20name%3D%22EMPTY%22%3EFALSE%3C/field%3E%3Cvalue%20name%3D%22ROI1%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22PXtX1nUz%3FP%21JNZ%3FE3.87%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7Es%29P0S@%24%24q%3Aig%3FKWZuvY%22%20variabletype%3D%22orsROI%22%3EaLRedgeROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22ROI2%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22k@YMywns%5Biq%3Fr%5EVWvb05%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22Xvr%7EX%2C%7E%21Kuh8Z04K1MFq%22%20variabletype%3D%22orsROI%22%3EHRedgeROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22@Y%23O+u+8TRXlqsL%23UsIv%22%3E%3Cfield%20name%3D%22TEXT%22%3EaLRedge-HRedge%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_roi_color%22%20id%3D%229%29a9L%24JA@%7E%5EtS4rz%5E%3F-M%22%3E%3Cvalue%20name%3D%22ROI%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%5BSo%3BCeRGpI%5EEufR_zuGg%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3Am%5B%7DN%5BXdsvViI%21ui0%21%28t%22%20variabletype%3D%22orsROI%22%3EHR_LR%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22COLOR%22%3E%3Cblock%20type%3D%22colour_picker%22%20id%3D%228eGA86xCsuAu%28qN@%5BUS0%22%3E%3Cfield%20name%3D%22COLOUR%22%3E%23339999%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_roi_color%22%20id%3D%22%28U%28dP3D%25ZdHGD%7E%3D%24eWgd%22%3E%3Cvalue%20name%3D%22ROI%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22M%3FCK/BbB9p.kA6cnMPgZ%22%3E%3Cmutation%20output_type_at_creation%3D%22orsROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22/D72K*e%7B.N@r*qFiqIha%22%20variabletype%3D%22orsROI%22%3EHR_aLR%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22COLOR%22%3E%3Cblock%20type%3D%22colour_picker%22%20id%3D%22%28bgg_%7Bl%28j4B5bw%3Fhg/K%3B%22%3E%3Cfield%20name%3D%22COLOUR%22%3E%23cc33cc%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22H@d0Zz8Ap44K%2C6%5Ea%3AYxI%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%3Am%5B%7DN%5BXdsvViI%21ui0%21%28t%22%20variabletype%3D%22orsROI%22%3EHR_LR%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22ors_model_publish_object%22%20id%3D%22G%7Ca70MT%7ETLg%60ndFb%3DEs1%22%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22/D72K*e%7B.N@r*qFiqIha%22%20variabletype%3D%22orsROI%22%3EHR_aLR%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22multiline_python_code%22%20id%3D%22l2f_q%60Ciut/%28X%24Z%28%29waU%22%3E%3Cmutation%20forcerender%3D%22true%22%3E%3C/mutation%3E%3Cfield%20name%3D%22CODE%22%3EaLR_HR_ndarray%20%3D%20HR_aLR.getNDArray%28%29%0ALR_HR_ndarray%20%3DHR_LR.getNDArray%28%29%0ALRedge_ndarray%20%3D%20LRedgeROI.getNDArray%28%29%0AaLRedge_ndarray%20%3D%20aLRedgeROI.getNDArray%28%29%0Aresult%20%3D%20%5B%27Baseline%20error%3A%20%27+str%28np.sum%28aLR_HR_ndarray%29/np.sum%28aLRedge_ndarray%29%29+%27%3B%20%20Registration%20error%3A%20%27+str%28np.sum%28LR_HR_ndarray%29/np.sum%28LRedge_ndarray%29%29%5D%0A%3C/field%3E%3Cnext%3E%3Cblock%20type%3D%22message_prompt%22%20id%3D%22%5E%239rX3_3%3A1kv7zDe02Cq%22%3E%3Cvalue%20name%3D%22TITLE%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22y%3BIxeTp%7EViOWHBEZR2%29M%22%3E%3Cfield%20name%3D%22TEXT%22%3ERegistration%20result%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22CAPTION%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22u0IMCc/%24%3Fv%2Cm%3FO4XQ%2Cs%21%22%3E%3Cfield%20name%3D%22TEXT%22%3ENote%3A%20Registration%20error%20%26lt%3B%20baseline%20error%20indicates%20acceptable%20alignment.%20%20%20%20%20%20%20%20%20%20%20%20%20%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22INPUT%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%7CudS-%2C%3FFk%7E5%5BTu%25u%3FDQV%22%3E%3Cmutation%20output_type_at_creation%3D%22str%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%7BfX%60Fz5HL-ZWL-yKc%5EB%2C%22%20variabletype%3D%22str%22%3Eresult%3C/field%3E%3Cfield%20name%3D%22type%22%3Estr%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/xml%3E
##### START OF BLOCKLY DEFINITIONS #####
from ORSServiceClass.ORSWidget.chooseObjectAndNewName.chooseObjectAndNewName import ChooseObjectAndNewName
import ORSModel
from ORSServiceClass.ORSWidget.SimpleEntryDialog.simpleEntryDialog import SimpleEntryDialog
import ORSModel
from OrsPythonPlugins.OrsVolumeROITools.OrsVolumeROITools import OrsVolumeROITools
from ORSServiceClass.preferencesapplier.preferencesApplyManager import PreferencesApplyManager
from ORSModel import Color
from OrsHelpers.roihelper import ROIHelper
from ORSModel.ors import ROI
from ORSServiceClass.messagebox.orsMessageBox import OrsTMessageBox

def get_object_from_chooser(tp: str, title: str):
        class_name = tp[3:]
        class_object = getattr(ORSModel, class_name)
        return ChooseObjectAndNewName.prompt([class_object], parent=WorkingContext.getCurrentContextWindow(), dialog_title=title, allowNone=True, getNewTitle=False)

def get_value(type: str, title: str, default: str):
    value = SimpleEntryDialog.prompt(None, type, title, default)
    if type == "Integer:":
        try:
            return int(value)
        except ValueError:
            return int(default)
    elif type == "Float:":
        try:
            return float(value)
        except ValueError:
            return float(default)
    elif type == "Text:":
        try:
            return str(value)
        except ValueError:
            return str(default)

def create_roi(channel, min, max, title, color):
    max = channel.getMaximumValue() if max > channel.getMaximumValue() else max
    min = channel.getMinimumValue() if min <= 0 else min
    roi = OrsVolumeROITools.createROIInRange(channel, title, min, max)
    if color is not None and color != "":
        #we have to convert the color from hex to our color model
        color = tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2 ,4))
        ROIColor = Color(color[0]/255, color[1]/255, color[2]/255, 0.5)
        PreferencesApplyManager.applyPreferencesOn(roi, defaultColor=ROIColor)
    return roi

def otsu_foreground(roi, dataset):
    roiBackground, roiForeground, _ = OrsVolumeROITools.splitAtOtsu(roi, dataset)
    if roiBackground is not None:
        roiBackground.deleteObject()
    return roiForeground

def boolean_operation(choice, roi1, roi2, title, keepEmpty):
    if isinstance(roi1, MultiROI):
        roiOrMR = MultiROI()
    else:
        roiOrMR = ROI()
    roiOrMR.copyShapeFromStructuredGrid(roi1)
    keepEmpty = True if keepEmpty == "true" else False
    if choice == "UNION":
        ROIHelper.union([roi1, roi2], roiOrMR, keepEmptyLabels=keepEmpty)
    elif choice == "INTERSECT":
        ROIHelper.intersection([roi1, roi2], roiOrMR, keepEmptyLabels=keepEmpty)
    elif choice == "AMINUSB":
        ROIHelper.subtract(roi1, roi2, roiOrMR, keepEmptyLabels=keepEmpty)
    elif choice == "REMOVE":
        ROIHelper.removeLabelIntersectingRoiOrMultiROI(roi1, [roi1, roi2], 0, roiOrMR)
    else:
        ROIHelper.keepLabelIntersectingRoiOrMultiROI(roi1, [roi1, roi2], 0, roiOrMR)
    if len(title) > 1:
        roiOrMR.setTitle(title)
    return roiOrMR

def show_msgbox(message, caption, title):
        message = str(caption) + str(message)
        OrsTMessageBox.message(None, message, str(title), OrsTMessageBox.Information, OrsTMessageBox.Ok)
##### END OF BLOCKLY DEFINITIONS #####


LRimage =  get_object_from_chooser('orsChannel', 'LRimage')
HRimage =  get_object_from_chooser('orsChannel', 'HRimage')
osf = OrsSimpleFilters()
osf.setFilter("f05bebb0ea3211e683dec86000a21918")
osf.setInputChannel(LRimage.getGUID(), 0)
osf.setIndexFirstVoxelInputChannel(0, 0, 0, 0, 0)
LRdenoise = Channel()
LRdenoise.copyShapeFromStructuredGrid(LRimage)
LRdenoise.initializeData()
osf.setOutputChannel(LRdenoise.getGUID(), 0)
osf.setIndexFirstVoxelOutputChannel(0, 0, 0, 0, 0)
setupDescription = """<description>
<inputChannelsCount>1</inputChannelsCount>
<outputChannelsCount>1</outputChannelsCount>
<kernelDim>3</kernelDim>
<kernelSize>{kernelSize}</kernelSize>
<kernelShape>'square'</kernelShape>
<booleanArguments>
</booleanArguments>
<numericArguments>
	<sigma>{sigma}</sigma>
</numericArguments>
<stringArguments>
</stringArguments>
</description>"""
formattedDescription = setupDescription.format(sigma=0.9999999999999999, kernelSize=3)
osf.setupFromDescription(formattedDescription)
osf.apply(0,0,0,0, LRimage.getXSize()-1, LRimage.getYSize()-1, LRimage.getZSize()-1, LRimage.getTSize()-1)
osf.deletePlugin()
osf = OrsSimpleFilters()
osf.setFilter("369fae80ea3c11e6a9f1c86000a21918")
osf.setInputChannel(LRdenoise.getGUID(), 0)
osf.setIndexFirstVoxelInputChannel(0, 0, 0, 0, 0)
LRimage_sobel = Channel()
LRimage_sobel.copyShapeFromStructuredGrid(LRdenoise)
LRimage_sobel.initializeData()
osf.setOutputChannel(LRimage_sobel.getGUID(), 0)
osf.setIndexFirstVoxelOutputChannel(0, 0, 0, 0, 0)
setupDescription = """<description>
<inputChannelsCount>1</inputChannelsCount>
<outputChannelsCount>1</outputChannelsCount>
<kernelDim>3</kernelDim>
<kernelShape>'square'</kernelShape>
<kernelSize>3</kernelSize>
<booleanArguments>
	<gaussian>True</gaussian>
</booleanArguments>
<numericArguments>
</numericArguments>
<stringArguments>
</stringArguments>
</description>"""
formattedDescription = setupDescription.format()
osf.setupFromDescription(formattedDescription)
osf.apply(0,0,0,0, LRdenoise.getXSize()-1, LRdenoise.getYSize()-1, LRdenoise.getZSize()-1, LRdenoise.getTSize()-1)
osf.deletePlugin()
osf = OrsSimpleFilters()
osf.setFilter("369fae80ea3c11e6a9f1c86000a21918")
osf.setInputChannel(HRimage.getGUID(), 0)
osf.setIndexFirstVoxelInputChannel(0, 0, 0, 0, 0)
HRimage_sobel = Channel()
HRimage_sobel.copyShapeFromStructuredGrid(HRimage)
HRimage_sobel.initializeData()
osf.setOutputChannel(HRimage_sobel.getGUID(), 0)
osf.setIndexFirstVoxelOutputChannel(0, 0, 0, 0, 0)
setupDescription = """<description>
<inputChannelsCount>1</inputChannelsCount>
<outputChannelsCount>1</outputChannelsCount>
<kernelDim>3</kernelDim>
<kernelShape>'square'</kernelShape>
<kernelSize>3</kernelSize>
<booleanArguments>
	<gaussian>True</gaussian>
</booleanArguments>
<numericArguments>
</numericArguments>
<stringArguments>
</stringArguments>
</description>"""
formattedDescription = setupDescription.format()
osf.setupFromDescription(formattedDescription)
osf.apply(0,0,0,0, HRimage.getXSize()-1, HRimage.getYSize()-1, HRimage.getZSize()-1, HRimage.getTSize()-1)
osf.deletePlugin()
osf = OrsSimpleFilters()
osf.setFilter("f05bebb0ea3211e683dec86000a21918")
osf.setInputChannel(HRimage.getGUID(), 0)
osf.setIndexFirstVoxelInputChannel(0, 0, 0, 0, 0)
HRgauss = Channel()
HRgauss.copyShapeFromStructuredGrid(HRimage)
HRgauss.initializeData()
osf.setOutputChannel(HRgauss.getGUID(), 0)
osf.setIndexFirstVoxelOutputChannel(0, 0, 0, 0, 0)
setupDescription = """<description>
<inputChannelsCount>1</inputChannelsCount>
<outputChannelsCount>1</outputChannelsCount>
<kernelDim>3</kernelDim>
<kernelSize>{kernelSize}</kernelSize>
<kernelShape>'square'</kernelShape>
<booleanArguments>
</booleanArguments>
<numericArguments>
	<sigma>{sigma}</sigma>
</numericArguments>
<stringArguments>
</stringArguments>
</description>"""
formattedDescription = setupDescription.format(sigma=get_value('Float:', 'Standard deviation', ''), kernelSize=get_value('Integer:', 'Kernel Size', ''))
osf.setupFromDescription(formattedDescription)
osf.apply(0,0,0,0, HRimage.getXSize()-1, HRimage.getYSize()-1, HRimage.getZSize()-1, HRimage.getTSize()-1)
osf.deletePlugin()
HRxSpacing = HRgauss.getXSpacing()
HRySpacing = HRgauss.getYSpacing()
HRzSpacing = HRgauss.getZSpacing()
HRgauss_sample = OrsDatasetSampler.sampleDatasetInSpacing(dataset=HRgauss, xSpacing=(HRxSpacing * 2), ySpacing=(HRySpacing * 2), zSpacing=(HRzSpacing * 2), samplingType=COMWrapper.ORS_def.CxvSamplingMethod.CxvSamplingNearest, createNewDataset=True)
HRgauss_sample.publish()
HRgauss_sample.setTitle('aLR image')
osf = OrsSimpleFilters()
osf.setFilter("369fae80ea3c11e6a9f1c86000a21918")
osf.setInputChannel(HRgauss_sample.getGUID(), 0)
osf.setIndexFirstVoxelInputChannel(0, 0, 0, 0, 0)
HRgauss_sample_sobel = Channel()
HRgauss_sample_sobel.copyShapeFromStructuredGrid(HRgauss_sample)
HRgauss_sample_sobel.initializeData()
osf.setOutputChannel(HRgauss_sample_sobel.getGUID(), 0)
osf.setIndexFirstVoxelOutputChannel(0, 0, 0, 0, 0)
setupDescription = """<description>
<inputChannelsCount>1</inputChannelsCount>
<outputChannelsCount>1</outputChannelsCount>
<kernelDim>3</kernelDim>
<kernelShape>'square'</kernelShape>
<kernelSize>3</kernelSize>
<booleanArguments>
	<gaussian>False</gaussian>
</booleanArguments>
<numericArguments>
</numericArguments>
<stringArguments>
</stringArguments>
</description>"""
formattedDescription = setupDescription.format()
osf.setupFromDescription(formattedDescription)
osf.apply(0,0,0,0, HRgauss_sample.getXSize()-1, HRgauss_sample.getYSize()-1, HRgauss_sample.getZSize()-1, HRgauss_sample.getTSize()-1)
osf.deletePlugin()
BOX =  get_object_from_chooser('orsVisualShape', 'Metrics box')
LRedge_extract = extractBoxFromChannel_bdfbc9a8110b11e8819130e37aed33ab.createDatasetFromVisualBox(sourceDataset=LRimage_sobel, visualBox=BOX, timestep=0, title='LR edge extract')

HRedge_extract = extractBoxFromChannel_bdfbc9a8110b11e8819130e37aed33ab.createDatasetFromVisualBox(sourceDataset=HRimage_sobel, visualBox=BOX, timestep=0, title='HR edge extract')

aLRedge_extract = extractBoxFromChannel_bdfbc9a8110b11e8819130e37aed33ab.createDatasetFromVisualBox(sourceDataset=HRgauss_sample_sobel, visualBox=BOX, timestep=0, title='aLR edge extract')

LRminFloat = LRedge_extract.getMinimumValue()
LRmaxFloat = LRedge_extract.getMaximumValue()
LRfullROI = create_roi(LRedge_extract, LRminFloat, LRmaxFloat, 'New ROI', None)

LRedgeROI = otsu_foreground(LRfullROI, LRedge_extract)

LRedgeROI.setTitle('LR edge ROI')
HRminFloat = HRedge_extract.getMinimumValue()
HRmaxFloat = HRedge_extract.getMaximumValue()
HRfullROI = create_roi(HRedge_extract, HRminFloat, HRmaxFloat, 'New ROI', None)

HRedgeROI = otsu_foreground(HRfullROI, HRedge_extract)

HRedgeROI.setTitle('HR edge ROI')
aLRminFloat = aLRedge_extract.getMinimumValue()
aLRmaxFloat = aLRedge_extract.getMaximumValue()
aLRfullROI = create_roi(aLRedge_extract, aLRminFloat, aLRmaxFloat, 'New ROI', None)

aLRedgeROI = otsu_foreground(aLRfullROI, aLRedge_extract)

aLRedgeROI.setTitle('aLR edge ROI')
LRedge_extract.publish()
HRedge_extract.publish()
aLRedge_extract.publish()
LRedgeROI.publish()
HRedgeROI.publish()
aLRedgeROI.publish()
if isinstance(HRimage_sobel, ORSModel.Managed):
    HRimage_sobel.deleteObject()
    del HRimage_sobel
else:
    del HRimage_sobel
if isinstance(LRdenoise, ORSModel.Managed):
    LRdenoise.deleteObject()
    del LRdenoise
else:
    del LRdenoise
if isinstance(LRimage_sobel, ORSModel.Managed):
    LRimage_sobel.deleteObject()
    del LRimage_sobel
else:
    del LRimage_sobel
if isinstance(HRgauss, ORSModel.Managed):
    HRgauss.deleteObject()
    del HRgauss
else:
    del HRgauss
if isinstance(HRgauss_sample_sobel, ORSModel.Managed):
    HRgauss_sample_sobel.deleteObject()
    del HRgauss_sample_sobel
else:
    del HRgauss_sample_sobel
if isinstance(HRfullROI, ORSModel.Managed):
    HRfullROI.deleteObject()
    del HRfullROI
else:
    del HRfullROI
if isinstance(LRfullROI, ORSModel.Managed):
    LRfullROI.deleteObject()
    del LRfullROI
else:
    del LRfullROI
if isinstance(aLRfullROI, ORSModel.Managed):
    aLRfullROI.deleteObject()
    del aLRfullROI
else:
    del aLRfullROI
HR_LR = boolean_operation('AMINUSB', LRedgeROI, HRedgeROI, 'LRedge-HRedge', 'false')

HR_aLR = boolean_operation('AMINUSB', aLRedgeROI, HRedgeROI, 'aLRedge-HRedge', 'false')

color = tuple(int('#339999'.lstrip("#")[i:i+2], 16) for i in (0, 2 ,4))
ROIColor = Color(color[0]/255, color[1]/255, color[2]/255, 0.5)
ROIHelper.setColor(HR_LR, ROIColor)
color = tuple(int('#cc33cc'.lstrip("#")[i:i+2], 16) for i in (0, 2 ,4))
ROIColor = Color(color[0]/255, color[1]/255, color[2]/255, 0.5)
ROIHelper.setColor(HR_aLR, ROIColor)
HR_LR.publish()
HR_aLR.publish()
aLR_HR_ndarray = HR_aLR.getNDArray()
LR_HR_ndarray =HR_LR.getNDArray()
LRedge_ndarray = LRedgeROI.getNDArray()
aLRedge_ndarray = aLRedgeROI.getNDArray()
result = ['Registration error: '+str(np.sum(LR_HR_ndarray)/np.sum(LRedge_ndarray))+';  Baseline error: '+str(np.sum(aLR_HR_ndarray)/np.sum(aLRedge_ndarray)*(np.sum(LRedge_ndarray)/np.sum(aLRedge_ndarray)))]


show_msgbox(result, 'Note: Registration error < Baseline error indicates acceptable alignment.             ', 'Registration result')
# ********** END MACRO ********** #

