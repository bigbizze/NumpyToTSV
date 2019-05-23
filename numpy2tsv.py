# Copyright 2019 Charles Anderson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
############################################################################################################################################################


class ConvertNumpy:
    def __init__(self, array, labels=None):
        """
        :param array: Numpy array of shape (num_samples, *n, data) where n is any number of dimensions.
        :param labels: A list of labels (one dimension only, will update later)
        """
        self.array = array
        self.labels = labels
        self.quote_all = False
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
        if self.quote_all:
            self.labels = ['"' + x + '"' for x in self.labels]
        data = self._join_generic_sep(self.labels, "\n")
        with open(filepath, "w") as fp:
            fp.write(data)

    def to_tsv(self, filepath, delim="\t", quote_all=False):
        """
        :param filepath: filepath to location to save .tsv file
        :param delim: delimiter to be used in output file, default '\t'
        :param quote_all: (bool) whether to quote each value
        :return: None
        """
        assert filepath.endswith(".tsv")
        self.quote_all = quote_all
        self._array_to(filepath, delim)

    def to_csv(self, filepath, delim=",", quote_all=False):
        """
         :param filepath: filepath to location to save .csv file
         :param delim: delimiter to be used in output file, default ','
         :param quote_all: (bool) whether to quote each value
         :return: None
         """
        assert filepath.endswith(".csv")
        self.quote_all = quote_all
        self._array_to(filepath, delim)

    def labels_to_tsv(self, filepath, quote_all=False):
        """
         :param filepath: filepath to location to save .tsv file
         :param quote_all: (bool) whether to quote each value
         :return: None
         """
        assert filepath.endswith(".tsv")
        self.quote_all = quote_all
        self._labels_to(filepath)

    def labels_to_csv(self, filepath, quote_all=False):
        """
         :param filepath: filepath to location to save .csv file
         :param quote_all: (bool) whether to quote each value
         :return: None
         """
        assert filepath.endswith(".csv")
        self.quote_all = quote_all
        self._labels_to(filepath)
