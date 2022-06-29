function loadGEData(data, ele) {

    createDefaultPanel(ele, `$ A = ${data.mat} $`);

    let content = '$A$';
    for(let i = 0; i < data.course.length; i++) {
        content = content + `$\\rightarrow ${data.course[i]}$`;
    }
    createDefaultPanel(ele, content);

}

function loadLinequData(data, ele) {

    createPanel(ele).text(`$AX = b，$其中$A=${data.mat}$，$b=${data.vec}$，记增广矩阵$C = (A, b)$`);

    let course = '$A$';
    for(let i = 0; i < data.elimination_course.length; i++) {
        course = course + `$\\rightarrow ${data.elimination_course[i]}$`;
    }
    createPanel(ele).text(course);
    
    if(data.solveset.length <= 0) {
        createPanel(ele).text('无解');
    } else {
        course = '';
        for(let i = 0; i < data.solveset.length; i++) {
            course = course + `x_${i+1} = & ${data.solveset[i]} \\\\`;
        }
        course = `$\\left\\{\\begin{matrix} ${course.substring(0, course.length - 3)} \\end{matrix}\\right.$`;
        createPanel(ele).text(course);
    }
}

function loadLambdaLinData(data, ele) {

    function creatRootCourse(data, i) {
        // 每行生成每个根的解方程过程
        
    
        let course = `当$ ${data.lam} = ${data.root[i]}$时，`;
        if(data.LQS_list[i].solveset.length == 0) {
            course += `$Rank(A)=${data.rank[i][0]}, Rank(C)=${data.rank[i][1]}$，所以无解`
        } else {
            course += `$Rank(A)=Rank(C)=${data.rank[i][0]}$，`
            let solveset = ''
            for(let j = 0; j < data.LQS_list[i].solveset.length; j++) {
                solveset += `x_${j+1} = & ${data.LQS_list[i].solveset[j]} \\\\`;
            }
            course += `解得$\\left\\{\\begin{matrix} ${solveset.substring(0, solveset.length-3)} \\end{matrix}\\right.$`;
        }
    
        createPanel(ele).text(course);

        createTogglePanel(ele, `solve${i}`, '展开详细解方程过程', '')
        loadLinequData(data.LQS_list[i], $(`#solve${i}`));
    }

    createPanel(ele).text(`$AX = b$，其中$A=${data.mA}$，$b=${data.mb}$，记增广矩阵$C = (A, b)$`);

    createPanel(ele).text(`$|A| = ${data.determinat} = ${data.factorization}$`);

    let course = '解方程$|A| = 0$，';
    if(data.root.length == 0) {
        course += '得方程无解，故原方程有唯一解'
        createPanel(ele).text(course);
    } else {
        course += '存在根'
        for(let i = 0; i < data.root.length; i++) {
            course += `,$${data.lam}_{${i+1}} = ${data.root[i]}$`;
        }
        createPanel(ele).text(course);

        for(let i = 0; i < data.root.length; i++) {
            creatRootCourse(data, i)
        }
    }

    course = ''
    for(let i = 0; i < data.LQS_nozero.solveset.length; i++) {
        course += `x_${i+1} = & ${data.LQS_nozero.solveset[i]} \\\\`;
    }
    course = `当$|A|=0$时，有唯一解： $$\\left\\{\\begin{matrix} ${course.substring(0, course.length-3)} \\end{matrix}\\right.$$`;
    createPanel(ele).text(course);

    createTogglePanel(ele, `solve_nozero`, '展开详细解方程过程', '')
    loadLinequData(data.LQS_nozero, $(`#solve_nozero`));
}

function loadDeterminantData(data, ele) {

    createDefaultPanel(ele, `$A = ${data.mat}$`);

    for(let i = 0; i < data.cofactor.length; i++) {
        let content = '=';

        if (data.operater[0][0] == '+') {
            content += `$ ${data.coef[0][0]} ${data.cofactor[0][0]} $`;
        } else {
            content += `$ ${data.operater[0][0]} ${data.coef[0][0]} ${data.cofactor[0][0]} $`;
        }

        for(let j = 1; j < data.cofactor[i].length; j++) {
            content += `$ ${data.operater[i][j]} ${data.coef[i][j]} ${data.cofactor[i][j]} $`;
        }
        createDefaultPanel(ele, content);
    }

    let content = '=';
    if (data.result_operater[0] == '+') {
        content += `$ ${data.result[0]} $`;
    } else {
        content += `$ ${data.result_operater[0]} ${data.result[0]} $`;
    }
    for(let i = 1; i < data.result.length; i++) {
        content += `$ ${data.result_operater[i]} ${data.result[i]} $`;
    }
    createDefaultPanel(ele, content);

    createDefaultPanel(ele, `=$ ${data.sum} $`);

}

function loadGaussDeterminantData(data, ele) {

    loadGEData(data.GES, ele);

    content = `A = ${data.factor[0]}`;
    for(let i = 1; i < data.factor.length; i++) {
        content += `\\times ${data.factor[i]}`;
    }
    createDefaultPanel(ele, `$ ${content} = ${data.result} $`);
}

function loadEigenValueData(data, ele) {
    createDefaultPanel(ele, `$ A = ${data.mat} $`);
    createDefaultPanel(ele, `$ |\\lambda E - A| = ${data.lambda_mat} = ${data.charpoly} $`);

    let content = `$  \\lambda_{1} = ${data.result[0][0]}  $`;
    for(let i = 1; i < data.result.length; i++) {
        content = content + `, $  \\lambda_{${i+1}} = ${data.result[i][0]} $`;
    }
    createDefaultPanel(ele, content);
}

function loadEigenVectorData(data, ele) {
    loadEigenValueData(data.EVAS, ele);

    for(let i = 0; i < data.result.length; i++) {
        createDefaultPanel(ele, `$ (\\lambda_{${i+1}} E - A)X = ${data.equ_mat[i]}X = 0 $`);

        let content = `解得：$  X_{${i+1}1} = ${data.result[i][0]}  $`;
        for(let j = 1; j < data.result[i].length; j++) {
            content = content + `, $ X_{${i+1}${j+1}} = ${data.result[i][j]} $`;
        }
        createDefaultPanel(ele, content);
    }
}

function loadDiagSymmetricData(data, ele) {
    loadEigenVectorData(data.EVES, ele);
    createDefaultPanel(ele, `$ D = T^{-1}AT, D = ${data.matD}, T = ${data.matT} $`)
}

function loadLincombinationData(data, ele) {
    let content = 'a_{0}';
    for(let i = 1; i < data.coef.length; i++) {
        content += `,a_{${i}}`;
    }
    content = `(${content})`;
    createDefaultPanel(ele, `解方程：$ ${content}X = b, ${content} = ${data.mat}, b = ${data.vec}$`);

    content = '';
    if(data.solveset.length <= 0) {
        content = '无解';
    } else {
        content = '';
        for(let i = 0; i < data.solveset.length; i++) {
            content = content + `x_${i+1} = & ${data.solveset[i]} \\\\`;
        }
        content = `$\\left\\{\\begin{matrix} ${content.substring(0, content.length - 3)} \\end{matrix}\\right.$`;
    }
    createDefaultPanel(ele, content);

    content = `b = ${data.coef[0]} a_{0}`;
    for(let i = 1; i < data.coef.length; i++) {
        content += `+ ${data.coef[i]} a_{${i}}`;
    }
    createDefaultPanel(ele, `代入未知元为0得：$ ${content} $`);
}

function loadLinDependenceData(data, ele) {
    createDefaultPanel(ele, `$A = ${data.mat}$`);
    GEPart(data.GES, ele)
    
    let content = '列不满秩，故线性无关';
    if(data.result) {
        content = '列满秩，故线性相关';
    }
    createDefaultPanel(ele, content);
}

function loadBasisTransData(data, ele) {
    createDefaultPanel(ele, `变换前的基$B = ${data.ma}$，变换后的基$C = ${data.mb}$`);
    createDefaultPanel(ele, `线性映射的矩阵$A = ${data.mat}$`);
    createDefaultPanel(ele, `过渡矩阵$ T = CB^{-1} = ${data.matT} $`);
    createDefaultPanel(ele, `变换后的矩阵$ D = T^{-1}AT = ${data.result} $`);
}

function loadHurwitzSolverData(data, ele) {
    createDefaultPanel(ele, `$ A = ${data.mat} $`);
    HurwitzPart(data, ele);
    let content = '$A$既不正定也不负定。';
    if(data.result == 'postive') {
        content = '所以$A$正定。';
    } else if(data.result == 'negative') {
        content = '所以$A$负定。';
    }
    createDefaultPanel(ele, content);

}

function loadPolyData(data, ele) {
    createDefaultPanel(ele, `多项式$ p = ${data.matPoly} $，矩阵$ A = ${data.mat} $`);
    createDefaultPanel(ele, `代入A到p得: $ p = ${data.subPoly}$`);
    createDefaultPanel(ele, `结果是: $p = ${data.result}$`);
}

function loadSchmidtPolyData(data, ele) {

    let content = '';
    for(let i = 0; i < data.group.length; i++) {
        content += `\\alpha_{${i+1}} = ${data.group[i]},`;
    }
    createDefaultPanel(ele, `初始向量：$${content.substring(0, content.length - 1)}$`);

    for(let i = 0; i < data.result.length; i++) {
        let content = `\\varepsilon_{${i+1}} = \\alpha_{${i+1}}`;
        for(let j = 0; j < i; j++) {
          content += `- \\frac{(\\alpha_{${i+1}}, \\varepsilon_{${j+1}})}{(\\varepsilon_{${i+1}}, \\varepsilon_{${j+1}})} \\varepsilon_{${j+1}}`;
        }
        content += `= \\alpha_{${i+1}}`;
        for(let j = 0; j < i; j++) {
          if (data.coef[i][j].charAt(0) == '-') {
            // 防止出现连续的两个负号
            content = content + `+ ${data.coef[i][j].substring(1)}\\varepsilon_{${j+1}}`;
          } else {
            content = content + `- ${data.coef[i][j]}\\varepsilon_{${j+1}}`;
          }
        }
        content += `= ${data.result[i]}`;
        createDefaultPanel(ele, `$$${content}$$`);
    }

    content = '';
    for(let i = 0; i < data.unitized.length; i++) {
      content = content + `\\varepsilon_{${i+1}}' = ${data.unitized[i]},`;
    }
    content = `单位化后得：$${content.substring(0, content.length - 1)}$`;
    createDefaultPanel(ele, content);
}