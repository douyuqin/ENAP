/***
* This code is a part of EvoApproxLib library (ehw.fit.vutbr.cz/approxlib) distributed under The MIT License.
* When used, please cite the following article(s):  
* This file contains a circuit from a sub-set of pareto optimal circuits with respect to the pwr and ep parameters
***/
// MAE% = 0.0024 %
// MAE = 1.6 
// WCE% = 0.0076 %
// WCE = 5.0 
// WCRE% = 300.00 %
// EP% = 78.12 %
// MRE% = 0.052 %
// MSE = 4.5 
// PDK45_PWR = 0.063 mW
// PDK45_AREA = 126.2 um2
// PDK45_DELAY = 1.11 ns
#include <stdint.h>
#include <stdlib.h>

uint64_t add16se_2BY(const uint64_t B,const uint64_t A)
{
   uint64_t dout_36, dout_37, dout_38, dout_39, dout_40, dout_41, dout_42, dout_43, dout_44, dout_45, dout_46, dout_47, dout_48, dout_49, dout_50, dout_51, dout_52, dout_53, dout_54, dout_55, dout_56, dout_57, dout_58, dout_59, dout_60, dout_61, dout_62, dout_63, dout_64, dout_68, dout_69, dout_70, dout_71, dout_72, dout_73, dout_74, dout_75, dout_76, dout_77, dout_78, dout_79, dout_80, dout_81, dout_82, dout_83, dout_84, dout_85, dout_88, dout_89, dout_90, dout_91, dout_92, dout_93, dout_94, dout_95, dout_96, dout_97, dout_98, dout_99, dout_100, dout_101, dout_102, dout_103, dout_104, dout_105, dout_106, dout_107, dout_108, dout_109, dout_110, dout_111, dout_114, dout_115, dout_116, dout_117, dout_118, dout_119, dout_120, dout_121, dout_122, dout_123, dout_124, dout_125, dout_126, dout_127, dout_128, dout_129, dout_130, dout_131, dout_132, dout_133, dout_134, dout_135, dout_136, dout_137, dout_138, dout_139, dout_140, dout_141, dout_142, dout_143;
   uint64_t O;

   dout_36=((A >> 2)&1)&((B >> 2)&1);
   dout_37=((A >> 2)&1)&((B >> 2)&1);
   dout_38=((A >> 3)&1)&((B >> 3)&1);
   dout_39=((A >> 3)&1)^((B >> 3)&1);
   dout_40=((A >> 4)&1)&((B >> 4)&1);
   dout_41=((A >> 4)&1)^((B >> 4)&1);
   dout_42=((A >> 5)&1)&((B >> 5)&1);
   dout_43=((A >> 5)&1)^((B >> 5)&1);
   dout_44=((A >> 6)&1)&((B >> 6)&1);
   dout_45=((A >> 6)&1)^((B >> 6)&1);
   dout_46=((A >> 7)&1)&((B >> 7)&1);
   dout_47=((A >> 7)&1)^((B >> 7)&1);
   dout_48=((A >> 8)&1)&((B >> 8)&1);
   dout_49=((A >> 8)&1)^((B >> 8)&1);
   dout_50=((A >> 9)&1)&((B >> 9)&1);
   dout_51=((A >> 9)&1)^((B >> 9)&1);
   dout_52=((A >> 10)&1)&((B >> 10)&1);
   dout_53=((A >> 10)&1)^((B >> 10)&1);
   dout_54=((A >> 11)&1)&((B >> 11)&1);
   dout_55=((A >> 11)&1)^((B >> 11)&1);
   dout_56=((A >> 12)&1)&((B >> 12)&1);
   dout_57=((A >> 12)&1)^((B >> 12)&1);
   dout_58=((A >> 13)&1)&((B >> 13)&1);
   dout_59=((A >> 13)&1)^((B >> 13)&1);
   dout_60=((A >> 14)&1)&((B >> 14)&1);
   dout_61=((A >> 14)&1)^((B >> 14)&1);
   dout_62=((A >> 15)&1)&((B >> 15)&1);
   dout_63=((A >> 15)&1)^((B >> 15)&1);
   dout_64=((A >> 15)&1)^((B >> 15)&1);
   dout_68=dout_41&dout_38;
   dout_69=dout_41&dout_39;
   dout_70=dout_40|dout_68;
   dout_71=dout_45&dout_42;
   dout_72=dout_45&dout_43;
   dout_73=dout_44|dout_71;
   dout_74=dout_49&dout_46;
   dout_75=dout_49&dout_47;
   dout_76=dout_48|dout_74;
   dout_77=dout_53&dout_50;
   dout_78=dout_53&dout_51;
   dout_79=dout_52|dout_77;
   dout_80=dout_57&dout_54;
   dout_81=dout_57&dout_55;
   dout_82=dout_56|dout_80;
   dout_83=dout_61&dout_58;
   dout_84=dout_61&dout_59;
   dout_85=dout_60|dout_83;
   dout_88=dout_72&dout_70;
   dout_89=dout_72&dout_69;
   dout_90=dout_73|dout_88;
   dout_91=dout_78&dout_76;
   dout_92=dout_78&dout_75;
   dout_93=dout_79|dout_91;
   dout_94=dout_84&dout_82;
   dout_95=dout_84&dout_81;
   dout_96=dout_85|dout_94;
   dout_97=dout_89&dout_36;
   dout_98=dout_90|dout_97;
   dout_99=dout_95&dout_93;
   dout_100=dout_95&dout_92;
   dout_101=dout_96|dout_99;
   dout_102=dout_100&dout_98;
   dout_103=dout_101|dout_102;
   dout_104=dout_92&dout_98;
   dout_105=dout_93|dout_104;
   dout_106=dout_69&dout_36;
   dout_107=dout_70|dout_106;
   dout_108=dout_75&dout_98;
   dout_109=dout_76|dout_108;
   dout_110=dout_81&dout_105;
   dout_111=dout_82|dout_110;
   dout_114=dout_39&dout_36;
   dout_115=dout_38|dout_114;
   dout_116=dout_43&dout_107;
   dout_117=dout_42|dout_116;
   dout_118=dout_47&dout_98;
   dout_119=dout_46|dout_118;
   dout_120=dout_51&dout_109;
   dout_121=dout_50|dout_120;
   dout_122=dout_55&dout_105;
   dout_123=dout_54|dout_122;
   dout_124=dout_59&dout_111;
   dout_125=dout_58|dout_124;
   dout_126=dout_63&dout_103;
   dout_127=dout_62|dout_126;
   dout_128=((B >> 1)&1)|((A >> 1)&1);
   dout_129=dout_37^0xFFFFFFFFFFFFFFFFU;
   dout_130=dout_39^dout_36;
   dout_131=dout_41^dout_115;
   dout_132=dout_43^dout_107;
   dout_133=dout_45^dout_117;
   dout_134=dout_47^dout_98;
   dout_135=dout_49^dout_119;
   dout_136=dout_51^dout_109;
   dout_137=dout_53^dout_121;
   dout_138=dout_55^dout_105;
   dout_139=dout_57^dout_123;
   dout_140=dout_59^dout_111;
   dout_141=dout_61^dout_125;
   dout_142=dout_63^dout_103;
   dout_143=dout_64^dout_127;

   O = 0;
   O |= (dout_134&1) << 0;
   O |= (dout_128&1) << 1;
   O |= (dout_129&1) << 2;
   O |= (dout_130&1) << 3;
   O |= (dout_131&1) << 4;
   O |= (dout_132&1) << 5;
   O |= (dout_133&1) << 6;
   O |= (dout_134&1) << 7;
   O |= (dout_135&1) << 8;
   O |= (dout_136&1) << 9;
   O |= (dout_137&1) << 10;
   O |= (dout_138&1) << 11;
   O |= (dout_139&1) << 12;
   O |= (dout_140&1) << 13;
   O |= (dout_141&1) << 14;
   O |= (dout_142&1) << 15;
   O |= (dout_143&1) << 16;
   return O;
}
