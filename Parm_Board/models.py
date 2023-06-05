# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AoiParameters(models.Model):
    idparameters = models.AutoField(primary_key=True)
    datetime = models.TextField(blank=True, null=True)
    pc_name = models.TextField(blank=True, null=True)
    pc_mac = models.TextField(blank=True, null=True)
    pc_ip = models.TextField(blank=True, null=True)
    file_path = models.TextField(blank=True, null=True)
    func_ip_or_mura_ip = models.TextField(blank=True, null=True)
    camera_ip = models.TextField(blank=True, null=True)
    model_name = models.TextField(blank=True, null=True)
    func_or_mura = models.TextField(blank=True, null=True)
    xml_file_name = models.TextField(blank=True, null=True)
    pattern_no = models.TextField(blank=True, null=True)
    threshold_bp = models.TextField(db_column='Threshold_BP', blank=True, null=True)  # Field name made lowercase.
    threshold_bp_low = models.TextField(db_column='Threshold_BP_Low', blank=True, null=True)  # Field name made lowercase.
    boundary_mulwidth_by = models.TextField(db_column='Boundary_MulWidth_BY', blank=True, null=True)  # Field name made lowercase.
    boundary_mulwidth_lx = models.TextField(db_column='Boundary_MulWidth_LX', blank=True, null=True)  # Field name made lowercase.
    boundary_mulwidth_rx = models.TextField(db_column='Boundary_MulWidth_RX', blank=True, null=True)  # Field name made lowercase.
    boundary_mulwidth_ty = models.TextField(db_column='Boundary_MulWidth_TY', blank=True, null=True)  # Field name made lowercase.
    boundarysubthreshold = models.TextField(db_column='BoundarySubThreshold', blank=True, null=True)  # Field name made lowercase.
    threshold_dp = models.TextField(db_column='Threshold_DP', blank=True, null=True)  # Field name made lowercase.
    threshold_dp_low = models.TextField(db_column='Threshold_DP_Low', blank=True, null=True)  # Field name made lowercase.
    areamax_bp = models.TextField(db_column='AreaMax_BP', blank=True, null=True)  # Field name made lowercase.
    areamax_dp = models.TextField(db_column='AreaMax_DP', blank=True, null=True)  # Field name made lowercase.
    areamin_bp = models.TextField(db_column='AreaMin_BP', blank=True, null=True)  # Field name made lowercase.
    areamin_dp = models.TextField(db_column='AreaMin_DP', blank=True, null=True)  # Field name made lowercase.
    pointenable = models.TextField(db_column='PointEnable', blank=True, null=True)  # Field name made lowercase.
    elongation_max = models.TextField(db_column='Elongation_Max', blank=True, null=True)  # Field name made lowercase.
    elongation_max_bldp = models.TextField(db_column='Elongation_Max_BLDP', blank=True, null=True)  # Field name made lowercase.
    elongation_max_dp = models.TextField(db_column='Elongation_Max_DP', blank=True, null=True)  # Field name made lowercase.
    elongation_min = models.TextField(db_column='Elongation_Min', blank=True, null=True)  # Field name made lowercase.
    elongation_min_bldp = models.TextField(db_column='Elongation_Min_BLDP', blank=True, null=True)  # Field name made lowercase.
    elongation_min_dp = models.TextField(db_column='Elongation_Min_DP', blank=True, null=True)  # Field name made lowercase.
    fullness_max = models.TextField(db_column='Fullness_Max', blank=True, null=True)  # Field name made lowercase.
    fullness_max_dp = models.TextField(db_column='Fullness_Max_DP', blank=True, null=True)  # Field name made lowercase.
    fullness_min = models.TextField(db_column='Fullness_Min', blank=True, null=True)  # Field name made lowercase.
    fullness_min_dp = models.TextField(db_column='Fullness_Min_DP', blank=True, null=True)  # Field name made lowercase.
    bp_fullness_downlimit = models.TextField(db_column='BP_Fullness_DownLimit', blank=True, null=True)  # Field name made lowercase.
    bp_fullness_uplimit = models.TextField(db_column='BP_Fullness_UpLimit', blank=True, null=True)  # Field name made lowercase.
    dp_fullness_downlimit = models.TextField(db_column='DP_Fullness_DownLimit', blank=True, null=True)  # Field name made lowercase.
    dp_fullness_uplimit = models.TextField(db_column='DP_Fullness_UpLimit', blank=True, null=True)  # Field name made lowercase.
    grayabnormalenable = models.TextField(db_column='GrayAbnormalEnable', blank=True, null=True)  # Field name made lowercase.
    removehvband = models.TextField(db_column='RemoveHVBand', blank=True, null=True)  # Field name made lowercase.
    blackmacromura_threshold = models.TextField(db_column='BlackMacroMura_Threshold', blank=True, null=True)  # Field name made lowercase.
    whitemacromura_threshold = models.TextField(db_column='WhiteMacroMura_Threshold', blank=True, null=True)  # Field name made lowercase.
    whiteblobmura_areamax = models.TextField(db_column='WhiteBlobMura_AreaMax', blank=True, null=True)  # Field name made lowercase.
    whiteblobmura_areamin = models.TextField(db_column='WhiteBlobMura_AreaMin', blank=True, null=True)  # Field name made lowercase.
    whiteblobmura_elongationmax = models.TextField(db_column='WhiteBlobMura_ElongationMax', blank=True, null=True)  # Field name made lowercase.
    whiteblobmura_elongationmin = models.TextField(db_column='WhiteBlobMura_ElongationMin', blank=True, null=True)  # Field name made lowercase.
    whiteblobmura_jndmax = models.TextField(db_column='WhiteBlobMura_JNDMax', blank=True, null=True)  # Field name made lowercase.
    whiteblobmura_jndmin = models.TextField(db_column='WhiteBlobMura_JNDMin', blank=True, null=True)  # Field name made lowercase.
    whiteagm_areamax = models.TextField(db_column='WhiteAGM_AreaMax', blank=True, null=True)  # Field name made lowercase.
    whiteagm_areamin = models.TextField(db_column='WhiteAGM_AreaMin', blank=True, null=True)  # Field name made lowercase.
    whiteagm_elongationmax = models.TextField(db_column='WhiteAGM_ElongationMax', blank=True, null=True)  # Field name made lowercase.
    whiteagm_elongationmin = models.TextField(db_column='WhiteAGM_ElongationMin', blank=True, null=True)  # Field name made lowercase.
    whiteagm_jndmax = models.TextField(db_column='WhiteAGM_JNDMax', blank=True, null=True)  # Field name made lowercase.
    whiteagm_jndmin = models.TextField(db_column='WhiteAGM_JNDMin', blank=True, null=True)  # Field name made lowercase.
    blackagm_areamax = models.TextField(db_column='BlackAGM_AreaMax', blank=True, null=True)  # Field name made lowercase.
    blackagm_areamin = models.TextField(db_column='BlackAGM_AreaMin', blank=True, null=True)  # Field name made lowercase.
    blackagm_elongationmax = models.TextField(db_column='BlackAGM_ElongationMax', blank=True, null=True)  # Field name made lowercase.
    blackagm_elongationmin = models.TextField(db_column='BlackAGM_ElongationMin', blank=True, null=True)  # Field name made lowercase.
    blackagm_jndmax = models.TextField(db_column='BlackAGM_JNDMax', blank=True, null=True)  # Field name made lowercase.
    blackagm_jndmin = models.TextField(db_column='BlackAGM_JNDMin', blank=True, null=True)  # Field name made lowercase.
    thresholdrim_bp = models.TextField(db_column='ThresholdRim_BP', blank=True, null=True)  # Field name made lowercase.
    thresholdrim_bp_low = models.TextField(db_column='ThresholdRim_BP_Low', blank=True, null=True)  # Field name made lowercase.
    thresholdrim_dp = models.TextField(db_column='ThresholdRim_DP', blank=True, null=True)  # Field name made lowercase.
    thresholdrim_dp_low = models.TextField(db_column='ThresholdRim_DP_Low', blank=True, null=True)  # Field name made lowercase.
    analysisbp = models.TextField(db_column='AnalysisBP', blank=True, null=True)  # Field name made lowercase.
    analysisdp = models.TextField(db_column='AnalysisDP', blank=True, null=True)  # Field name made lowercase.
    poslimit = models.TextField(db_column='PosLimit', blank=True, null=True)  # Field name made lowercase.
    neglimit = models.TextField(db_column='NegLimit', blank=True, null=True)  # Field name made lowercase.
    blackblobmura_areamax = models.TextField(db_column='BlackBlobMura_AreaMax', blank=True, null=True)  # Field name made lowercase.
    blackblobmura_areamin = models.TextField(db_column='BlackBlobMura_AreaMin', blank=True, null=True)  # Field name made lowercase.
    blackblobmura_elongationmax = models.TextField(db_column='BlackBlobMura_ElongationMax', blank=True, null=True)  # Field name made lowercase.
    blackblobmura_elongationmin = models.TextField(db_column='BlackBlobMura_ElongationMin', blank=True, null=True)  # Field name made lowercase.
    blackblobmura_jndmax = models.TextField(db_column='BlackBlobMura_JNDMax', blank=True, null=True)  # Field name made lowercase.
    blackblobmura_jndmin = models.TextField(db_column='BlackBlobMura_JNDMin', blank=True, null=True)  # Field name made lowercase.
    patternname = models.TextField(db_column='PatternName', blank=True, null=True)  # Field name made lowercase.
    pattern_enable = models.IntegerField(db_column='Pattern_Enable', blank=True, null=True)  # Field name made lowercase.
    line_cut = models.TextField(db_column='Line_Cut', blank=True, null=True)  # Field name made lowercase.
    line_short_cut = models.TextField(db_column='Line_Short_Cut', blank=True, null=True)  # Field name made lowercase.
    line_cut_h = models.TextField(db_column='Line_Cut_H', blank=True, null=True)  # Field name made lowercase.
    line_short_cut_h = models.TextField(db_column='Line_Short_Cut_H', blank=True, null=True)  # Field name made lowercase.
    lineenable = models.TextField(db_column='LineEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aoi_parameters'
