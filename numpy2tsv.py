class ConvertNumpy:
    def __init__(self, array, labels=None, quote_all=False):
        self.array = array
        self.labels = labels
        self.quote_all = quote_all
        self.num_dims = len(self.array.shape)
        self.dim_lens = [self.array.shape[x] for x in range(self.num_dims)]
        self.num_labels = len(self.labels)
        assert self.dim_lens[0] == self.num_labels

    @staticmethod
    def _join_generic_sep(x, delim):
        return delim.join(x)

    def _recurse_loop(self, amounts, depth, data, data_out, delim):
        temp_list = list()
        for i in range(amounts[-depth]):
            data_temp = data[i]
            if depth != 1:
                temp = self._recurse_loop(amounts, depth - 1, data_temp, data_out, delim)
                data_out.append(temp)
            else:
                temp_data = str(data_temp) if not self.quote_all else '"' + str(data_temp) + '"'
                temp_list.append(temp_data)
        return self._join_generic_sep(temp_list, delim=delim) if depth == 1 else self._join_generic_sep(data_out, "\n")

    def _array_to(self, filepath, delim):
        out_data = list()
        data = self._recurse_loop(self.dim_lens, self.num_dims, self.array, out_data, delim)
        with open(filepath, "w") as fp:
            fp.write(data)

    def _labels_to(self, filepath):
        data = self._join_generic_sep(self.labels, "\n")
        with open(filepath, "w") as fp:
            fp.write(data)

    def to_tsv(self, filepath, delim="\t"):
        assert filepath.endswith(".tsv")
        self._array_to(filepath, delim)

    def to_csv(self, filepath, delim=","):
        assert filepath.endswith(".csv")
        self._array_to(filepath, delim)

    def labels_to_tsv(self, filepath):
        assert filepath.endswith(".tsv")
        self._labels_to(filepath)

    def labels_to_csv(self, filepath):
        assert filepath.endswith(".csv")
        self._labels_to(filepath)