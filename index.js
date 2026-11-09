
/*function ArrayIntersection(arr1, arr2) {

    const set2 = new Set(arr2);

    return [...new Set(arr1.filter(x => set2.has(x)))];

}
*/

function ArrayIntersection (arr1, arr2) {

    const a = [...arr1].sort((x,y) => x - y);

    const b = [...arr2].sort((x,y) => x - y);

    const result = [];

    let i = 0, j = 0;

    while (i < a.length && j < b.length){

        if (a[i] == b[j]){

            if (result[result.length - 1] != a[i]) result.push(a[i]);

            i++;
            j++;

        }else if (a[i] < b[j]){

            i++;

        }else {
            j++;
        }
    }

    return result;
}

function LongestConsecutive(arr){

    const set = new Set(arr);

    let maior = 0;

    for (const n of set) {

        if (!set.has(n - 1)){

            let atual = n;

            let tamanho  = 1;

            while (set.has(atual + 1)){

                atual++;
                tamanho++;
            }

            if (tamanho > maior) maior = tamanho;

        }
    }
    
    return maior;

}


function main () {

    let arr1 = [1,2,3,4];
    let arr2 = [3,4,5,6];

    console.log(ArrayIntersection(arr1,arr2));

}

console.log(main());
