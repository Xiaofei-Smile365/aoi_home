import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict

from .models import AoiParameters

import datetime


def index(request):
    # 获取1个小时内的数据
    hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1000000)
    current_time = datetime.datetime.now()
    current_1_hour_objs = AoiParameters.objects.filter(datetime__gt=hour_ago, datetime__lt=current_time,
                                                       pattern_enable=0)

    pc_name_set = set()
    for i in current_1_hour_objs:
        pc_name_set.add(i.pc_name)
    pc_name_list = sorted(list(pc_name_set), reverse=False)

    camera_ip_set = set()
    for i in current_1_hour_objs:
        camera_ip_set.add(i.camera_ip)
    camera_ip_list = sorted(list(camera_ip_set), reverse=False)

    model_name_set = set()
    for i in current_1_hour_objs:
        model_name_set.add(i.model_name)
    model_name_list = sorted(list(model_name_set), reverse=False)

    func_ip_or_mura_ip_set = set()
    for i in current_1_hour_objs:
        func_ip_or_mura_ip_set.add(i.func_ip_or_mura_ip)
    func_ip_or_mura_ip_list = sorted(list(func_ip_or_mura_ip_set), reverse=False)

    pattern_name_set = set()
    for i in current_1_hour_objs:
        pattern_name_set.add(i.patternname)
    pattern_name_list = sorted(list(pattern_name_set), reverse=False)

    context = {"pc_name_list": pc_name_list, "camera_ip_list": camera_ip_list, "model_name_list": model_name_list,
               "func_ip_or_mura_ip_list": func_ip_or_mura_ip_list, "pattern_name_list": pattern_name_list}
    return render(request, 'Parm_Board/index.html', context)


def search_linkage_pc_name(request):
    pc_name = request.GET.get('pc_name')
    # 获取1个小时内的数据
    hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1000000)
    current_time = datetime.datetime.now()
    search_pc_name_current_1_hour_objs = AoiParameters.objects.filter(datetime__gt=hour_ago, datetime__lt=current_time,
                                                                      pattern_enable=0, pc_name=pc_name)

    data = {'camera_ip': [], 'model_name': [], 'func_ip_or_mura_ip': [], 'pattern_name': []}

    camera_ip_set = set()
    for i in search_pc_name_current_1_hour_objs:
        camera_ip_set.add(i.camera_ip)
    camera_ip_list = sorted(list(camera_ip_set), reverse=False)

    for camera_ip in camera_ip_list:
        data['camera_ip'].append({'camera_ip': camera_ip})

    model_name_set = set()
    for i in search_pc_name_current_1_hour_objs:
        model_name_set.add(i.model_name)
    model_name_list = sorted(list(model_name_set), reverse=False)

    for model_name in model_name_list:
        data['model_name'].append({'model_name': model_name})

    func_ip_or_mura_ip_set = set()
    for i in search_pc_name_current_1_hour_objs:
        func_ip_or_mura_ip_set.add(i.func_ip_or_mura_ip)
    func_ip_or_mura_ip_list = sorted(list(func_ip_or_mura_ip_set), reverse=False)

    for func_ip_or_mura_ip in func_ip_or_mura_ip_list:
        data['func_ip_or_mura_ip'].append({'func_ip_or_mura_ip': func_ip_or_mura_ip})

    pattern_name_set = set()
    for i in search_pc_name_current_1_hour_objs:
        pattern_name_set.add(i.patternname)
    pattern_name_list = sorted(list(pattern_name_set), reverse=False)

    for pattern_name in pattern_name_list:
        data['pattern_name'].append({'pattern_name': pattern_name})

    return JsonResponse(data)


def search_linkage_camera_ip(request):
    pc_name = request.GET.get('pc_name')
    camera_ip = request.GET.get('camera_ip')
    # 获取1个小时内的数据
    hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1000000)
    current_time = datetime.datetime.now()
    search_camera_ip_current_1_hour_objs = AoiParameters.objects.filter(datetime__gt=hour_ago,
                                                                        datetime__lt=current_time,
                                                                        pattern_enable=0, pc_name=pc_name,
                                                                        camera_ip=camera_ip)

    data = {'pc_name': [], 'model_name': [], 'func_ip_or_mura_ip': [], 'pattern_name': []}

    pc_name_set = set()
    for i in search_camera_ip_current_1_hour_objs:
        pc_name_set.add(i.pc_name)
    pc_name_list = sorted(list(pc_name_set), reverse=False)

    for pc_name in pc_name_list:
        data['pc_name'].append({'pc_name': pc_name})

    model_name_set = set()
    for i in search_camera_ip_current_1_hour_objs:
        model_name_set.add(i.model_name)
    model_name_list = sorted(list(model_name_set), reverse=False)

    for model_name in model_name_list:
        data['model_name'].append({'model_name': model_name})

    func_ip_or_mura_ip_set = set()
    for i in search_camera_ip_current_1_hour_objs:
        func_ip_or_mura_ip_set.add(i.func_ip_or_mura_ip)
    func_ip_or_mura_ip_list = sorted(list(func_ip_or_mura_ip_set), reverse=False)

    for func_ip_or_mura_ip in func_ip_or_mura_ip_list:
        data['func_ip_or_mura_ip'].append({'func_ip_or_mura_ip': func_ip_or_mura_ip})

    pattern_name_set = set()
    for i in search_camera_ip_current_1_hour_objs:
        pattern_name_set.add(i.patternname)
    pattern_name_list = sorted(list(pattern_name_set), reverse=False)

    for pattern_name in pattern_name_list:
        data['pattern_name'].append({'pattern_name': pattern_name})

    return JsonResponse(data)


def search_linkage_model_name(request):
    pc_name = request.GET.get('pc_name')
    camera_ip = request.GET.get('camera_ip')
    func_ip_or_mura_ip = request.GET.get('func_ip_or_mura_ip')
    model_name = request.GET.get('model_name')
    # 获取1个小时内的数据
    hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1000000)
    current_time = datetime.datetime.now()
    search_model_name_current_1_hour_objs = AoiParameters.objects.filter(datetime__gt=hour_ago,
                                                                         datetime__lt=current_time,
                                                                         pattern_enable=0,
                                                                         pc_name=pc_name,
                                                                         camera_ip=camera_ip,
                                                                         func_ip_or_mura_ip=func_ip_or_mura_ip,
                                                                         model_name=model_name)

    data = {'pc_name': [], 'camera_ip': [], 'func_ip_or_mura_ip': [], 'pattern_name': []}

    pc_name_set = set()
    for i in search_model_name_current_1_hour_objs:
        pc_name_set.add(i.pc_name)
    pc_name_list = sorted(list(pc_name_set), reverse=False)

    for pc_name in pc_name_list:
        data['pc_name'].append({'pc_name': pc_name})

    camera_ip_set = set()
    for i in search_model_name_current_1_hour_objs:
        camera_ip_set.add(i.camera_ip)
    camera_ip_list = sorted(list(camera_ip_set), reverse=False)

    for camera_ip in camera_ip_list:
        data['camera_ip'].append({'camera_ip': camera_ip})

    func_ip_or_mura_ip_set = set()
    for i in search_model_name_current_1_hour_objs:
        func_ip_or_mura_ip_set.add(i.func_ip_or_mura_ip)
    func_ip_or_mura_ip_list = sorted(list(func_ip_or_mura_ip_set), reverse=False)

    for func_ip_or_mura_ip in func_ip_or_mura_ip_list:
        data['func_ip_or_mura_ip'].append({'func_ip_or_mura_ip': func_ip_or_mura_ip})

    pattern_name_set = set()
    for i in search_model_name_current_1_hour_objs:
        pattern_name_set.add(i.patternname)
    pattern_name_list = sorted(list(pattern_name_set), reverse=False)

    for pattern_name in pattern_name_list:
        data['pattern_name'].append({'pattern_name': pattern_name})

    return JsonResponse(data)


def search_linkage_func_ip_or_mura_ip(request):
    pc_name = request.GET.get('pc_name')
    camera_ip = request.GET.get('camera_ip')
    func_ip_or_mura_ip = request.GET.get('func_ip_or_mura_ip')
    # 获取1个小时内的数据
    hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1000000)
    current_time = datetime.datetime.now()
    search_func_ip_or_mura_ip_current_1_hour_objs = AoiParameters.objects.filter(datetime__gt=hour_ago,
                                                                                 datetime__lt=current_time,
                                                                                 pattern_enable=0,
                                                                                 pc_name=pc_name,
                                                                                 camera_ip=camera_ip,
                                                                                 func_ip_or_mura_ip=func_ip_or_mura_ip)

    data = {'pc_name': [], 'camera_ip': [], 'model_name': [], 'pattern_name': []}

    pc_name_set = set()
    for i in search_func_ip_or_mura_ip_current_1_hour_objs:
        pc_name_set.add(i.pc_name)
    pc_name_list = sorted(list(pc_name_set), reverse=False)

    for pc_name in pc_name_list:
        data['pc_name'].append({'pc_name': pc_name})

    camera_ip_set = set()
    for i in search_func_ip_or_mura_ip_current_1_hour_objs:
        camera_ip_set.add(i.camera_ip)
    camera_ip_list = sorted(list(camera_ip_set), reverse=False)

    for camera_ip in camera_ip_list:
        data['camera_ip'].append({'camera_ip': camera_ip})

    model_name_set = set()
    for i in search_func_ip_or_mura_ip_current_1_hour_objs:
        model_name_set.add(i.model_name)
    model_name_list = sorted(list(model_name_set), reverse=False)

    for model_name in model_name_list:
        data['model_name'].append({'model_name': model_name})

    pattern_name_set = set()
    for i in search_func_ip_or_mura_ip_current_1_hour_objs:
        pattern_name_set.add(i.patternname)
    pattern_name_list = sorted(list(pattern_name_set), reverse=False)

    for pattern_name in pattern_name_list:
        data['pattern_name'].append({'pattern_name': pattern_name})

    return JsonResponse(data)


def search_linkage_pattern_name(request):
    pc_name = request.GET.get('pc_name')
    camera_ip = request.GET.get('camera_ip')
    func_ip_or_mura_ip = request.GET.get('func_ip_or_mura_ip')
    model_name = request.GET.get('model_name')
    pattern_name = request.GET.get('pattern_name')
    # 获取1个小时内的数据
    hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1000000)
    current_time = datetime.datetime.now()
    search_pattern_name_current_1_hour_objs = AoiParameters.objects.filter(datetime__gt=hour_ago,
                                                                           datetime__lt=current_time,
                                                                           pattern_enable=0,
                                                                           pc_name=pc_name,
                                                                           camera_ip=camera_ip,
                                                                           func_ip_or_mura_ip=func_ip_or_mura_ip,
                                                                           model_name=model_name,
                                                                           patternname=pattern_name)

    data = {'pc_name': [], 'camera_ip': [], 'model_name': [], 'func_ip_or_mura_ip': []}

    pc_name_set = set()
    for i in search_pattern_name_current_1_hour_objs:
        pc_name_set.add(i.pc_name)
    pc_name_list = sorted(list(pc_name_set), reverse=False)

    for pc_name in pc_name_list:
        data['pc_name'].append({'pc_name': pc_name})

    camera_ip_set = set()
    for i in search_pattern_name_current_1_hour_objs:
        camera_ip_set.add(i.camera_ip)
    camera_ip_list = sorted(list(camera_ip_set), reverse=False)

    for camera_ip in camera_ip_list:
        data['camera_ip'].append({'camera_ip': camera_ip})

    model_name_set = set()
    for i in search_pattern_name_current_1_hour_objs:
        model_name_set.add(i.model_name)
    model_name_list = sorted(list(model_name_set), reverse=False)

    for model_name in model_name_list:
        data['model_name'].append({'model_name': model_name})

    func_ip_or_mura_ip_set = set()
    for i in search_pattern_name_current_1_hour_objs:
        func_ip_or_mura_ip_set.add(i.func_ip_or_mura_ip)
    func_ip_or_mura_ip_list = sorted(list(func_ip_or_mura_ip_set), reverse=False)

    for func_ip_or_mura_ip in func_ip_or_mura_ip_list:
        data['func_ip_or_mura_ip'].append({'func_ip_or_mura_ip': func_ip_or_mura_ip})

    return JsonResponse(data)


def search(request):
    if request.method == 'GET':
        # 处理提交事件
        pc_name = request.GET.get("pc_name")
        camera_ip = request.GET.get("camera_ip")
        func_ip_or_mura_ip = request.GET.get("func_ip_or_mura_ip")
        model_name = request.GET.get("model_name")
        pattern_name = request.GET.get("pattern_name")

        # 获取1个小时内的数据
        hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1000000)
        current_time = datetime.datetime.now()
        selected_current_1_hour_objs = AoiParameters.objects.filter(datetime__gt=hour_ago, datetime__lt=current_time,
                                                                    pattern_enable=0, pc_name=pc_name,
                                                                    camera_ip=camera_ip,
                                                                    func_ip_or_mura_ip=func_ip_or_mura_ip,
                                                                    model_name=model_name,
                                                                    patternname=pattern_name)
        parm_data = []
        for parm in selected_current_1_hour_objs:
            parm_data.append(model_to_dict(parm))
        data = json.dumps(parm_data[-1])
        return HttpResponse(data)
