from converter import app
from ..util.operations_file import zip_files
import json
import copy


def check_dict_in_list(some_list: list):
    for i in some_list:
        if isinstance(i, dict):
            return True
    return False


def get_the_values(list_json: dict, csv_v, csv_temp):
    for json in list_json:
        csv_v.append(get_the_value([json], csv_temp))
        csv_temp = []
    return csv_v


def get_the_value(json: dict, csv_temp):
    for k, v in json.items():
        if isinstance(v, dict):
            return get_the_value(v, csv_temp)
        csv_temp.append(v)
    return csv_temp


def correct_key(key):
    return key.replace('rrd.', '').replace('params.', '').replace('.ds', '')


def get_the_keys(some_json: dict, csv_k):
    for k, v in some_json.items():
        if isinstance(v, dict):
            v = {correct_key(f'{k}.{k_in}'): v_in for k_in, v_in in v.items()}
            get_the_keys(v, csv_k)
        if isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    i = {correct_key(f'{k}.{k_in}')
                                     : i_in for k_in, i_in in i.items()}
                    get_the_keys(i, csv_k)

        if k not in csv_k and clean_keys(k):
            csv_k.append(k)
    return csv_k


def clean_keys(k):
    if 'cdp_prep' in k or 'database' in k or 'params' in k:
        return False
    if k == 'ds' or k == 'rra' or k == 'rrd':
        return False
    return True


def get_general_info(data):
    return [data['rrd']['version'], data['rrd']['step'], data['rrd']['lastupdate']]


def get_ds(data):
    ds_list = []
    for ds in data['rrd']['ds']:
        ds_list.append([v for v in ds.values()])
    return ds_list


def get_key_pipe_value(ds):
    return [f'{k_ds}|{v_ds}' for k_ds, v_ds in ds.items()]


def get_rra(data):
    rra_all = []
    for rra in data['rrd']['rra']:
        rra_list = []
        for k, v in rra.items():
            if k == 'params':
                rra_list.append(rra['params']['xff'])
                continue

            if k == 'cdp_prep':
                temp = []
                for ds in rra['cdp_prep']['ds']:
                    temp.append(get_key_pipe_value(ds))
                rra_list.append(temp)
                continue

            if k == 'database':
                continue
            rra_list.append(v)
        rra_all.append(rra_list)
    return rra_all


def get_database(data):
    database_list = []
    rra_list = []
    for rra in data['rrd']['rra']:
        for row in rra['database']['row']:
            rra_list.append(row['v'])
        database_list.append(rra_list)
    return database_list


def generate_csv_ds(filename, keys, general_info, ds, rra_list):
    file = open(f"{app.config['UPLOAD_FOLDER']}/{filename}_ds.csv", 'a')
    headers = ', '.join(keys)
    general_info = ', '.join(general_info)
    ds_traff_in = ', '.join(ds[0])
    ds_traff_out = ', '.join(ds[1])
    file.write(f'{headers}\n')
    for rra in rra_list:
        rra[3] = f"({', '.join(rra[3][0])})" + f"| ({', '.join(rra[3][1])})"
        rra_str = ', '.join(rra)
        line_in = f'{general_info}, {ds_traff_in}, {rra_str}'
        line_out = f'{general_info}, {ds_traff_out}, {rra_str}'
        file.write(f'{line_in}\n')
        file.write(f'{line_out}\n')
    file.close()


def generate_csv_database(filename, keys, rra_list, database_list):
    file = open(f"{app.config['UPLOAD_FOLDER']}/{filename}_database.csv", 'a')

    new_keys = copy.deepcopy(keys)
    for k in keys:
        if 'rra' not in k:
            new_keys.remove(k)

    new_keys.append('rra.database')
    headers = ', '.join(new_keys)
    file.write(f'{headers}\n')

    for rra, database in zip(rra_list, database_list):
        rra[3] = f"({', '.join(rra[3][0])})" + f"|({', '.join(rra[3][1])})"
        rra_str = ', '.join(rra)

        for data in database:
            database_str = '| '.join(data)
            file.write(f'{rra_str}, ({database_str})\n')
    file.close()


def generate_csv_file(filename, deleted_keys):
    data = json.loads(
        open(f"{app.config['UPLOAD_FOLDER']}/{filename}.json").read())
    keys = get_the_keys(data, list())
    keys.append('rra.cdp_prep')
    general_info = get_general_info(data)
    ds = get_ds(data)
    rra_list = get_rra(data)
    database_list = get_database(data)

    generate_csv_ds(filename, keys, general_info, ds, copy.deepcopy(rra_list))
    generate_csv_database(filename, keys, copy.deepcopy(
        rra_list), copy.deepcopy(database_list))

    zip_files(filename, f'{filename}_ds.csv', f'{filename}_database.csv')
