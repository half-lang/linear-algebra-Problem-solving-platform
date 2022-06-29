function createPanel(ele) {
    // 生成一个面板，用于显示一行解题过程
    // ele是面板所在的html元素

    let layer1 = $('<div class="panel panel-default"></div>');
    let layer2 = $('<div class="panel-body"></div>');
    let layer3 = $('<p></p>');

    $(ele).append(layer1);
    layer1.append(layer2);
    layer2.append(layer3);

    return layer3
}

function createButtonPanel(ele) {
    // 生成一个带按钮面板
    // ele是面板所在的html元素

    let layer1 = $('<div class="panel panel-default"></div>');
    let layer2 = $('<div class="panel-body"></div>');
    let layer3 = $('<div class="row"></div>');
    let layer4 = $('<div class="col-md-10"></div>');
    let layer5 = $('<div class="col-md-2"></div>');
    let layer6 = $('<p></p>');
    let layer7 = $('<button class="btn btn-default"></button>');

    $(ele).append(layer1);
    layer1.append(layer2);
    layer2.append(layer3);
    layer3.append(layer4);
    layer3.append(layer5);
    layer4.append(layer6);
    layer5.append(layer7);

    return [layer6, layer7];
}

function createTogglePanel(ele, id, title, content) {
    // 生成一个可折叠的面板
    // ele是面板所在的html元素 id指定折叠模板的id title指定折叠面板的标题 content指定折叠模板的内容
    // 生成之后可以用id找到该元素的body部分

    let panel = $(`<div class="panel panel-default"><div class="panel-heading"><a data-toggle="collapse" href="#${id}-toggle"></a></div><div id="${id}-toggle" class="panel-collapse collapse"><div class="panel-body" id="${id}"></div></div></div>`);

    panel.find('a').text(title);
    $(panel).find('.panel-body').append(content);
    $(ele).append(panel);
}

function createDefaultPanel(ele, content) {
    // 生成一个普通面板，是createPanel的改写
    // ele是面板所在的html元素

    let panel = $(`<div class="panel panel-default"><div class="panel-body"></div></div>`);
    panel.find('.panel-body').append(content);
    $(ele).append(panel);
}