#!/usr/bin/env python3


# +
# instrument(s)
# -
INS__NODES = {
    '90Prime': {
        'binning': 'None, 1x1, 2x2, 3x3, 4x4',
        'dither': 'None, NxM, n-RA, n-Dec',
        'filters': 'U, B, V, R, I, Clear',
        'flat_exposure_times': {'U': 30.0, 'B': 29.0, 'V': 28.0, 'R': 27.0, 'I': 26.0, 'Clear': 25.0},
        'readout': 15.0,
        'readout_times': {'None': 15.0, '2x2': 7.5, '3x3': 5.0, '4x4': 3.75},
        'telescope': 'Bok',
        'type': 'imager'
    },
    'BCSpec': {
        'binning': 'None, 1x1, 2x2, 3x3, 4x4',
        'filters': 'U, B, V, R, I, Clear',
        'flat_exposure_times': {'U': 30.0, 'B': 29.0, 'V': 28.0, 'R': 27.0, 'I': 26.0, 'Clear': 25.0},
        'readout': 15.0,
        'readout_times': {'None': 15.0, '2x2': 7.5, '3x3': 5.0, '4x4': 3.75},
        'slits': '1pix, 2pix, 3pix',
        'telescope': 'Bok',
        'type': 'spectrograph'
    },
    'Mont4k': {
        'binning': 'None, 1x1, 2x2, 3x3, 4x4',
        'dither': 'None, NxM, n-RA, n-Dec',
        'filters': 'U, B, V, R, I, Clear',
        'flat_exposure_times': {'U': 30.0, 'B': 29.0, 'V': 28.0, 'R': 27.0, 'I': 26.0, 'Clear': 25.0},
        'readout': 17.0,
        'readout_times': {'None': 20.0, '2x2': 10.0, '3x3': 6.5, '4x4': 5.0},
        'telescope': 'Kuiper',
        'type': 'imager'
    },
    'BinoSpec': {
        'binning': 'None, 1x1, 2x2, 3x3, 4x4',
        'filters': 'g, r, i, z, Clear',
        'flat_exposure_times': {'U': 30.0, 'B': 29.0, 'V': 28.0, 'R': 27.0, 'I': 26.0, 'Clear': 25.0},
        'readout': 15.0,
        'readout_times': {'None': 15.0, '2x2': 7.5, '3x3': 5.0, '4x4': 3.75},
        'slits': '1pix, 2pix, 3pix',
        'telescope': 'MMT',
        'type': 'spectrograph'
    },
    'Vatt4k': {
        'binning': 'None, 1x1, 2x2, 3x3, 4x4',
        'dither': 'None, NxM, n-RA, n-Dec',
        'filters': 'U, B, V, R, I, Clear',
        'flat_exposure_times': {'U': 30.0, 'B': 29.0, 'V': 28.0, 'R': 27.0, 'I': 26.0, 'Clear': 25.0},
        'readout': 20.0,
        'readout_times': {'None': 20.0, '2x2': 10.0, '3x3': 6.5, '4x4': 5.0},
        'telescope': 'Vatt',
        'type': 'imager'
    }
}


# +
# structure(s)
# -
INS__BINNING = {_k: _v['binning'] for _k, _v in INS__NODES.items() if 'binning' in _v}
INS__DITHER = {_k: _v['dither'] for _k, _v in INS__NODES.items() if 'dither' in _v}
INS__FILTERS = {_k: _v['filters'] for _k, _v in INS__NODES.items() if 'filters' in _v}
INS__FLAT__EXPOSURE__TIMES = {_k: INS__NODES[_k]['flat_exposure_times'] for _k, _v in INS__NODES.items()}
INS__NAME = [_k.lower() for _k in INS__NODES]
INS__READOUT = {_k: _v['readout'] for _k, _v in INS__NODES.items() if 'readout' in _v}
INS__READOUT__TIMES = {_k: INS__NODES[_k]['readout_times'] for _k, _v in INS__NODES.items()}
INS__SLITS = {_k: _v['slits'] for _k, _v in INS__NODES.items() if 'slits' in _v}
INS__TELESCOPE = {_k: _v['telescope'] for _k, _v in INS__NODES.items() if 'telescope' in _v}
INS__TYPE = {_k: _v['type'] for _k, _v in INS__NODES.items() if 'type' in _v}


# +
# function: get_supported(s)
# -
def get_supported(nodes=None):
    nodes = INS__NODES if (nodes is None or not isinstance(nodes, dict) or nodes is {}) else nodes
    _i, _s = {_k: _v['telescope'] for _k, _v in nodes.items()}, {}
    for _k, _v in _i.items():
        if _v not in _s:
            _s[_v] = [f"{_k}"]
        else:
            _s[_v].append(f"{_k}")
    return _s


# +
# derived structure(s)
# -
INS__INSTRUMENTS = [_k for _k in INS__NODES]
INS__TELESCOPES = sorted(set([_v['telescope'] for _k, _v in INS__NODES.items()]))
INS__SUPPORTED = get_supported(nodes=INS__NODES)
