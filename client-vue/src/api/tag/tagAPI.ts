import { ref, computed } from "vue";
import axios, { type AxiosInstance } from "axios";
import { type Tag } from "@/assets/types/tag";

const API: AxiosInstance = axios.create({
    baseURL: "http://localhost:8000",
});

export const getTags = async (userId: number): Promise<Tag[]> => {
    const { data } = await API.get<Tag[]>(`/tag/user/${userId}/`);
    return data;
};

export const createTag = async (payload: Omit<Tag, "id">): Promise<Tag> => {
    const { data } = await API.post<Tag>(`/tag/add`, payload);
    return data;
};

export const deleteTag = async (id: number): Promise<void> => {
    await API.delete(`/tag/delete/${id}/`);
};
