function search_parm(){
    let pc_name=$("#pc_name option:selected").val();// 获取当前选择项.
    let camera_ip=$("#camera_ip option:selected").val();// 获取当前选择项.
    let func_ip_or_mura_ip=$("#func_ip_or_mura_ip option:selected").val();// 获取当前选择项.
    let model_name=$("#model_name option:selected").val();// 获取当前选择项.
    let pattern_name=$("#pattern_name option:selected").val();// 获取当前选择项.
    // console.log(pc_name, camera_ip, func_ip_or_mura_ip, model_name, pattern_name)

    if (pc_name === '' || camera_ip === '' || func_ip_or_mura_ip === '' || model_name === '' || pattern_name === '') {
      window.alert("Please select.");
      return;
    }
    $.ajax({
        url: '/search/',
        method: 'get',
        async: false,
        data: {'pc_name':pc_name,'camera_ip':camera_ip,'func_ip_or_mura_ip':func_ip_or_mura_ip,'model_name':model_name,'pattern_name':pattern_name},
        success: function (data) {
            data = JSON.parse(data);
            // console.log(data);
            // console.log(data['threshold_bp']);

            document.getElementById('parm_func_abnormal_check_abnormal_data_refresh_time').innerHTML = `Data Refresh Time: ${ data['datetime'] }`;
            document.getElementById('parm_func_point_bp_point_threshold_bp').innerHTML = `Threshold BP: ${ data['threshold_bp'] }`;
            document.getElementById('parm_func_point_bp_point_threshold_bp_low').innerHTML = `Threshold BP Low: ${ data['threshold_bp_low'] }`;
            document.getElementById('parm_func_point_bp_point_thresholdrim_bp').innerHTML = `ThresholdRim BP: ${ data['thresholdrim_bp'] }`;
            document.getElementById('parm_func_point_bp_point_thresholdrim_bp_low').innerHTML = `ThresholdRim BP Low: ${ data['thresholdrim_bp_low'] }`;
            document.getElementById('parm_func_point_dp_point_threshold_dp').innerHTML = `Threshold DP: ${ data['threshold_dp'] }`;
            document.getElementById('parm_func_point_dp_point_threshold_dp_low').innerHTML = `Threshold DP Low: ${ data['threshold_dp_low'] }`;
            document.getElementById('parm_func_point_dp_point_thresholdrim_dp').innerHTML = `ThresholdRim DP: ${ data['thresholdrim_dp'] }`;
            document.getElementById('parm_func_point_dp_point_thresholdrim_dp_low').innerHTML = `ThresholdRim DP Low: ${ data['thresholdrim_dp_low'] }`;
            document.getElementById('parm_func_point_point_point_common_setting_areamax_bp').innerHTML = `AreaMax BP: ${ data['areamax_bp'] }`;
            document.getElementById('parm_func_point_point_point_common_setting_areamin_bp').innerHTML = `AreaMin BP: ${ data['areamin_bp'] }`;
            document.getElementById('parm_func_point_point_point_common_setting_areamax_dp').innerHTML = `AreaMax DP: ${ data['areamax_dp'] }`;
            document.getElementById('parm_func_point_point_point_common_setting_areamin_dp').innerHTML = `AreaMin DP: ${ data['areamin_dp'] }`;
            document.getElementById('parm_func_point_point_enable_point_enable').innerHTML = `Point Enable: ${ data['pointenable'] }`;
            document.getElementById('parm_func_point_point_enable_analysis_bp').innerHTML = `Analysis BP: ${ data['analysisbp'] }`;
            document.getElementById('parm_func_point_point_enable_analysis_dp').innerHTML = `Analysis DP: ${ data['analysisdp'] }`;
            document.getElementById('parm_func_point_characteristics_bp_characteristics_elongation_min').innerHTML = `Elongation Min: ${ data['elongation_min'] }`;
            document.getElementById('parm_func_point_characteristics_bp_characteristics_elongation_max').innerHTML = `Elongation Max: ${ data['elongation_max'] }`;
            document.getElementById('parm_func_point_characteristics_bp_characteristics_fullness_min').innerHTML = `Fullness Min: ${ data['fullness_min'] }`;
            document.getElementById('parm_func_point_characteristics_bp_characteristics_fullness_max').innerHTML = `Fullness Max: ${ data['fullness_max'] }`;
            document.getElementById('parm_func_point_characteristics_dp_characteristics_elongation_min_dp').innerHTML = `Elongation Min DP: ${ data['elongation_min_dp'] }`;
            document.getElementById('parm_func_point_characteristics_dp_characteristics_elongation_max_dp').innerHTML = `Elongation Max DP: ${ data['elongation_max_dp'] }`;
            document.getElementById('parm_func_point_characteristics_dp_characteristics_fullness_min_dp').innerHTML = `Fullness Min DP: ${ data['fullness_min_dp'] }`;
            document.getElementById('parm_func_point_characteristics_dp_characteristics_fullness_max_dp').innerHTML = `Fullness Max DP: ${ data['fullness_max_dp'] }`;
            document.getElementById('parm_func_abnormal_check_abnormal_gray_abnormal_enable').innerHTML = `Gray Abnormal Enable: ${ data['grayabnormalenable'] }`;
            document.getElementById('parm_func_abnormal_check_abnormal_poslimit').innerHTML = `PosLimit: ${ data['poslimit'] }`;
            document.getElementById('parm_func_abnormal_check_abnormal_neglimit').innerHTML = `NegLimit: ${ data['neglimit'] }`;
            document.getElementById('parm_func_abnormal_line_line_cut_v').innerHTML = `Line Cut V: ${ data['line_cut'] }`;
            document.getElementById('parm_func_abnormal_line_line_short_cut_v').innerHTML = `Line Short Cut V: ${ data['line_short_cut'] }`;
            document.getElementById('parm_func_abnormal_line_line_cut_h').innerHTML = `Line Cut H: ${ data['line_cut_h'] }`;
            document.getElementById('parm_func_abnormal_line_line_short_cut_h').innerHTML = `Line Short Cut H: ${ data['line_short_cut_h'] }`;
            document.getElementById('parm_func_abnormal_line_line_enable').innerHTML = `Line Enable: ${ data['lineenable'] }`;
            document.getElementById('parm_mura_center_by_pass_parm_white_white_macro_mura_threshold').innerHTML = `WhiteMacroMura Threshold: ${ data['whitemacromura_threshold'] }`;
            document.getElementById('parm_mura_center_by_pass_parm_black_black_macro_mura_threshold').innerHTML = `BlackMacroMura Threshold: ${ data['blackmacromura_threshold'] }`;
            document.getElementById('parm_mura_light_check_loss_point_parm_removehvband_removehvband').innerHTML = `Remove HV Band: ${ data['removehvband'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_blob_mura_areamin').innerHTML = `WhiteBlobMura AreaMin: ${ data['whiteblobmura_areamin'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_blob_mura_areamax').innerHTML = `WhiteBlobMura AreaMax: ${ data['whiteblobmura_areamax'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_blob_mura_jndmin').innerHTML = `WhiteBlobMura JndMin: ${ data['whiteblobmura_jndmin'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_blob_mura_jndmax').innerHTML = `WhiteBlobMura JNDMax: ${ data['whiteblobmura_jndmax'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_blob_mura_elongationmin').innerHTML = `WhiteBlobMura ElongationMin: ${ data['whiteblobmura_elongationmin'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_blob_mura_elongationmax').innerHTML = `WhiteBlobMura ElongationMax: ${ data['whiteblobmura_elongationmax'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_agm_areamin').innerHTML = `WhiteAGM AreaMin: ${ data['whiteagm_areamin'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_agm_areamax').innerHTML = `WhiteAGM AreaMax: ${ data['whiteagm_areamax'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_agm_jndmin').innerHTML = `WhiteAGM JndMin: ${ data['whiteagm_jndmin'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_agm_jndmax').innerHTML = `WhiteAGM JNDMax: ${ data['whiteagm_jndmax'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_agm_elongationmin').innerHTML = `WhiteAGM ElongationMin: ${ data['whiteagm_elongationmin'] }`;
            document.getElementById('parm_mura_white_mura_setting_white_blob_mura_white_agm_elongationmax').innerHTML = `WhiteAGM ElongationMax: ${ data['whiteagm_elongationmax'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_blob_mura_areamin').innerHTML = `BlackBlobMura AreaMin: ${ data['blackblobmura_areamin'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_blob_mura_areamax').innerHTML = `BlackBlobMura AreaMax: ${ data['blackblobmura_areamax'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_blob_mura_jndmin').innerHTML = `BlackBlobMura JndMin: ${ data['blackblobmura_jndmin'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_blob_mura_jndmax').innerHTML = `BlackBlobMura JNDMax: ${ data['blackblobmura_jndmax'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_blob_mura_elongationmin').innerHTML = `BlackBlobMura ElongationMin: ${ data['blackblobmura_elongationmin'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_blob_mura_elongationmax').innerHTML = `BlackBlobMura ElongationMax: ${ data['blackblobmura_elongationmax'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_agm_areamin').innerHTML = `BlackAGM AreaMin: ${ data['blackagm_areamin'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_agm_areamax').innerHTML = `BlackAGM AreaMax: ${ data['blackagm_areamax'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_agm_jndmin').innerHTML = `BlackAGM JndMin: ${ data['blackagm_jndmin'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_agm_jndmax').innerHTML = `BlackAGM JNDMax: ${ data['blackagm_jndmax'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_agm_elongationmin').innerHTML = `BlackAGM ElongationMin: ${ data['blackagm_elongationmin'] }`;
            document.getElementById('parm_mura_black_mura_setting_black_blob_mura_black_agm_elongationmax').innerHTML = `BlackAGM ElongationMax: ${ data['blackagm_elongationmax'] }`;
        }
    })
}