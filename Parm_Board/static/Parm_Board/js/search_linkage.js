$(document).ready(function() {
  $('#pc_name').change(function() {
    let pc_name = $(this).val();
    if (pc_name === '') {
      window.alert("Please select PC Name.");
      return;
    }

    $.ajax({
      url: '/search_linkage_pc_name/',
      data: {
        'pc_name': pc_name
      },
      dataType: 'json',
      success: function(data) {
        let options = '<option value=""></option>';
        for (let i = 0; i < data.camera_ip.length; i++) {
          options += '<option value="' + data.camera_ip[i].camera_ip + '">' + data.camera_ip[i].camera_ip + '</option>';
          // window.alert(data.camera_ip[i].camera_ip);
        }
        $('#camera_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.model_name.length; i++) {
          options += '<option value="' + data.model_name[i].model_name + '">' + data.model_name[i].model_name + '</option>';
          // window.alert(data.model_name[i].model_name);
        }
        $('#model_name').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.func_ip_or_mura_ip.length; i++) {
          options += '<option value="' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '">' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '</option>';
          // window.alert(data.func_ip_or_mura_ip[i].func_ip_or_mura_ip);
        }
        $('#func_ip_or_mura_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.pattern_name.length; i++) {
          options += '<option value="' + data.pattern_name[i].pattern_name + '">' + data.pattern_name[i].pattern_name + '</option>';
          // window.alert(data.pattern_name[i].pattern_name);
        }
        $('#pattern_name').html(options);
      }
    });
  });
});

$(document).ready(function() {
  $('#camera_ip').change(function() {
    let camera_ip = $(this).val();
    if ($("#pc_name option:selected").val() === '' || camera_ip === '') {
      window.alert("筛选器存在联动功能，请依次重新选择.");
      location.reload();
    }

    $.ajax({
      url: '/search_linkage_camera_ip/',
      data: {
        'pc_name': $("#pc_name option:selected").val(),
        'camera_ip': camera_ip
      },
      dataType: 'json',
      success: function(data) {
        let options = '<option value=""></option>';
        for (let i = 0; i < data.pc_name.length; i++) {
          options += '<option value="' + data.pc_name[i].pc_name + '">' + data.pc_name[i].pc_name + '</option>';
          // window.alert(data.pc_name[i].pc_name);
        }
        // $('#pc_name').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.model_name.length; i++) {
          options += '<option value="' + data.model_name[i].model_name + '">' + data.model_name[i].model_name + '</option>';
          // window.alert(data.model_name[i].model_name);
        }
        $('#model_name').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.func_ip_or_mura_ip.length; i++) {
          options += '<option value="' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '">' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '</option>';
          // window.alert(data.func_ip_or_mura_ip[i].func_ip_or_mura_ip);
        }
        $('#func_ip_or_mura_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.pattern_name.length; i++) {
          options += '<option value="' + data.pattern_name[i].pattern_name + '">' + data.pattern_name[i].pattern_name + '</option>';
          // window.alert(data.pattern_name[i].pattern_name);
        }
        $('#pattern_name').html(options);
      }
    });
  });
});

$(document).ready(function() {
  $('#model_name').change(function() {
    let model_name = $(this).val();
    if ($("#pc_name option:selected").val() === '' || $("#camera_ip option:selected").val() === '' || $("#func_ip_or_mura_ip option:selected").val() === '' || model_name === '') {
      window.alert("筛选器存在联动功能，请依次重新选择.");
      location.reload();
    }

    $.ajax({
      url: '/search_linkage_model_name/',
      data: {
        'pc_name': $("#pc_name option:selected").val(),
        'camera_ip': $("#camera_ip option:selected").val(),
        'func_ip_or_mura_ip':$("#func_ip_or_mura_ip option:selected").val(),
        'model_name': model_name
      },
      dataType: 'json',
      success: function(data) {
        let options = '<option value=""></option>';
        for (let i = 0; i < data.pc_name.length; i++) {
          options += '<option value="' + data.pc_name[i].pc_name + '">' + data.pc_name[i].pc_name + '</option>';
          // window.alert(data.pc_name[i].pc_name);
        }
        // $('#pc_name').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.camera_ip.length; i++) {
          options += '<option value="' + data.camera_ip[i].camera_ip + '">' + data.camera_ip[i].camera_ip + '</option>';
          // window.alert(data.camera_ip[i].camera_ip);
        }
        // $('#camera_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.func_ip_or_mura_ip.length; i++) {
          options += '<option value="' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '">' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '</option>';
          // window.alert(data.func_ip_or_mura_ip[i].func_ip_or_mura_ip);
        }
        // $('#func_ip_or_mura_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.pattern_name.length; i++) {
          options += '<option value="' + data.pattern_name[i].pattern_name + '">' + data.pattern_name[i].pattern_name + '</option>';
          // window.alert(data.pattern_name[i].pattern_name);
        }
        $('#pattern_name').html(options);
      }
    });
  });
});

$(document).ready(function() {
  $('#func_ip_or_mura_ip').change(function() {
    let func_ip_or_mura_ip = $(this).val();
    if ($("#pc_name option:selected").val() === '' || $("#camera_ip option:selected").val() === '' || func_ip_or_mura_ip === '') {
      window.alert("筛选器存在联动功能，请依次重新选择.");
      location.reload();
    }

    $.ajax({
      url: '/search_linkage_func_ip_or_mura_ip/',
      data: {
        'pc_name': $("#pc_name option:selected").val(),
        'camera_ip': $("#camera_ip option:selected").val(),
        'func_ip_or_mura_ip': func_ip_or_mura_ip
      },
      dataType: 'json',
      success: function(data) {
        let options = '<option value=""></option>';
        for (let i = 0; i < data.pc_name.length; i++) {
          options += '<option value="' + data.pc_name[i].pc_name + '">' + data.pc_name[i].pc_name + '</option>';
          // window.alert(data.pc_name[i].pc_name);
        }
        // $('#pc_name').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.camera_ip.length; i++) {
          options += '<option value="' + data.camera_ip[i].camera_ip + '">' + data.camera_ip[i].camera_ip + '</option>';
          // window.alert(data.camera_ip[i].camera_ip);
        }
        // $('#camera_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.model_name.length; i++) {
          options += '<option value="' + data.model_name[i].model_name + '">' + data.model_name[i].model_name + '</option>';
          // window.alert(data.model_name[i].model_name);
        }
        $('#model_name').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.pattern_name.length; i++) {
          options += '<option value="' + data.pattern_name[i].pattern_name + '">' + data.pattern_name[i].pattern_name + '</option>';
          // window.alert(data.pattern_name[i].pattern_name);
        }
        $('#pattern_name').html(options);
      }
    });
  });
});

$(document).ready(function() {
  $('#pattern_name').change(function() {
    let pattern_name = $(this).val();
    if ($("#pc_name option:selected").val() === '' || $("#camera_ip option:selected").val() === '' || $("#func_ip_or_mura_ip option:selected").val() === '' || $("#model_name option:selected").val() === '' || pattern_name === '') {
      window.alert("筛选器存在联动功能，请依次重新选择.");
      location.reload();
    }

    $.ajax({
      url: '/search_linkage_pattern_name/',
      data: {
        'pc_name': $("#pc_name option:selected").val(),
        'camera_ip': $("#camera_ip option:selected").val(),
        'func_ip_or_mura_ip':$("#func_ip_or_mura_ip option:selected").val(),
        'model_name':$("#model_name option:selected").val(),
        'pattern_name': pattern_name
      },
      dataType: 'json',
      success: function(data) {
        let options = '<option value=""></option>';
        for (let i = 0; i < data.pc_name.length; i++) {
          options += '<option value="' + data.pc_name[i].pc_name + '">' + data.pc_name[i].pc_name + '</option>';
          // window.alert(data.pc_name[i].pc_name);
        }
        // $('#pc_name').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.camera_ip.length; i++) {
          options += '<option value="' + data.camera_ip[i].camera_ip + '">' + data.camera_ip[i].camera_ip + '</option>';
          // window.alert(data.camera_ip[i].camera_ip);
        }
        // $('#camera_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.func_ip_or_mura_ip.length; i++) {
          options += '<option value="' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '">' + data.func_ip_or_mura_ip[i].func_ip_or_mura_ip + '</option>';
          // window.alert(data.func_ip_or_mura_ip[i].func_ip_or_mura_ip);
        }
        // $('#func_ip_or_mura_ip').html(options);

        options = '<option value=""></option>';
        for (let i = 0; i < data.model_name.length; i++) {
          options += '<option value="' + data.model_name[i].model_name + '">' + data.model_name[i].model_name + '</option>';
          // window.alert(data.model_name[i].model_name);
        }
        // $('#model_name').html(options);
      }
    });
  });
});
