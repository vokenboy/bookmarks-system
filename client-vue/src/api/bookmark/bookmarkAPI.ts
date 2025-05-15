import { ref, computed } from "vue";
import axios, { type AxiosInstance } from "axios";
import { type Bookmark } from "@/assets/types/bookmark";

const API: AxiosInstance = axios.create({
    baseURL: "http://localhost:8000",
});

export const getBookmarks = async (userId: number): Promise<Bookmark[]> => {
    const { data } = await API.get<Bookmark[]>(`/bookmark/user/${userId}/`);
    return data;
};

export const getBookmark = async (id: number): Promise<Bookmark> => {
    const response = await API.get<Bookmark>(`/bookmark/get/${id}`);
    return response.data;
};

export interface NewBookmarkPayload {
    name: string;
    link: string;
    description: string;
    user: number;
    tag_ids: number[];
    ws_ids?: number[];
}

export const createBookmark = async (
    payload: NewBookmarkPayload
): Promise<Bookmark> => {
    const { data } = await API.post<Bookmark>(`/bookmark/add/`, payload);
    return data;
};

export const deleteBookmark = async (id: number): Promise<void> => {
    await API.delete(`/bookmark/delete/${id}`);
};
